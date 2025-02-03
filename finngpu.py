import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import re
import argparse
import time
from pathlib import Path
from datetime import datetime
from tqdm import tqdm
from config import *

class RateLimiter:
    """Simple time-based rate limiter"""
    def __init__(self, max_calls_per_second: int):
        self.min_interval = 1.0 / max_calls_per_second
        self.last_call = 0

    def __call__(self):
        now = time.time()
        time_since_last = now - self.last_call
        if time_since_last < self.min_interval:
            time.sleep(self.min_interval - time_since_last)
        self.last_call = time.time()

def load_gpu_models():
    """Load GPU models from JSON file"""
    try:
        with open(MODELS_FILE) as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: {MODELS_FILE} not found")
        return []

def load_filter_list(filename: Path, list_type: str):
    """Load blacklist or whitelist from file"""
    filter_list = {'patterns': [], 'ids': []}
    try:
        with open(filename) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    if line.isdigit():
                        filter_list['ids'].append(line)
                    else:
                        filter_list['patterns'].append(line.lower())
    except FileNotFoundError:
        print(f"Warning: {list_type} file {filename} not found, proceeding without it")
    return filter_list

def match_gpu_model(text: str, gpu_models: list, debug=False) -> tuple:
    """Match GPU model with multiple GPU detection"""
    text = text.lower()
    if debug:
        print(f"\nProcessing text: {text}")

    pattern = r'\b(?:(?:geforce|nvidia|rtx|gtx|radeon|rx|intel\s*arc|arc)\s*)?([a]?\d{3,4})\s*[-\s]*(ti|xt|xtx|gre|super|s)?\s*(?:(\d+)\s*gb)?\b'
    matches = list(re.finditer(pattern, text))

    if debug:
        print(f"Regex matches found: {len(matches)}")
        for m in matches:
            print(f"Match groups: {m.groups()}")
            print(f"Full match: '{m.group(0)}'")
            print(f"Context: '...{text[max(0, m.start()-20):m.end()+20]}...'")

    if not matches:
        return "Unknown", None, None, None, None, 0

    # Process all matches
    all_matched_gpus = []

    for match in matches:
        number = match.group(1)
        suffix = match.group(2) or ''
        vram = match.group(3)

        # Standardize 's' to 'super'
        if suffix.lower() == 's':
            suffix = 'super'

        prefix = text[match.start():match.start(1)].strip()
        brand = 'NVIDIA' if any(x in prefix for x in ['geforce', 'nvidia', 'rtx', 'gtx']) else \
               'AMD' if any(x in prefix for x in ['radeon', 'rx']) else \
               'Intel' if any(x in prefix for x in ['intel arc', 'arc']) else None

        model_number = f"{number} {suffix}".strip()

        if debug:
            print(f"\nProcessing match:")
            print(f"  Number: {number}")
            print(f"  Suffix: {suffix}")
            print(f"  Brand: {brand}")
            print(f"  VRAM: {vram}")
            print(f"  Model number: {model_number}")

        # Special case for RTX 2060
        if number == "2060" and not suffix:
            found_2060_match = False
            for gpu in gpu_models:
                gpu_lower = gpu.lower()
                # Only match base 2060 6GB model if no explicit VRAM is specified in the title
                if "2060" in gpu_lower and "6 gb" in gpu_lower and "super" not in gpu_lower:
                    # Only add if no VRAM was specified or if specified VRAM matches
                    if not vram or vram == "6":
                        all_matched_gpus.append((gpu, brand, "2060", "6", "2060"))
                        found_2060_match = True
                        break
            if found_2060_match:
                continue

        exact_matches = []
        base_model_matches = []

        for gpu in gpu_models:
            gpu_lower = gpu.lower()
            if debug:
                print(f"\nChecking against GPU: {gpu_lower}")

            # Brand check
            if brand:
                gpu_brand = 'NVIDIA' if any(x in gpu_lower for x in ['geforce', 'rtx', 'gtx']) else \
                           'AMD' if any(x in gpu_lower for x in ['radeon', 'rx']) else \
                           'Intel' if any(x in gpu_lower for x in ['intel arc', 'arc']) else None
                if gpu_brand and brand != gpu_brand:
                    if debug:
                        print(f"  Skipping due to brand mismatch: {brand} != {gpu_brand}")
                    continue

            if suffix:
                # If input has a suffix, only look for exact matches
                if re.search(rf'\b{model_number}\b', gpu_lower):
                    if debug:
                        print(f"  Found exact match with suffix!")
                    if vram:
                        vram_match = re.search(rf'{vram}\s*gb', gpu_lower)
                        if not vram_match:
                            if debug:
                                print(f"  Skipping due to VRAM mismatch")
                            continue
                    exact_matches.append(gpu)
            else:
                # If input has no suffix, only match against base models (no suffix)
                if not re.search(r'\b(ti|xt|xtx|gre|super)\b', gpu_lower):
                    if re.search(rf'\b{number}\b', gpu_lower):
                        if debug:
                            print(f"  Found base model match!")
                        if vram:
                            vram_match = re.search(rf'{vram}\s*gb', gpu_lower)
                            if not vram_match:
                                if debug:
                                    print(f"  Skipping due to VRAM mismatch")
                                continue
                        base_model_matches.append(gpu)
                else:
                    if debug:
                        print(f"  Skipping variant model because input has no suffix")

        # Use exact matches if found, otherwise use base matches
        matches_for_this_gpu = exact_matches if exact_matches else base_model_matches

        if matches_for_this_gpu:
            if len(matches_for_this_gpu) == 1:
                all_matched_gpus.append((matches_for_this_gpu[0], brand, model_number, vram, model_number))
            else:
                # If multiple matches for this specific GPU pattern, add all of them
                for gpu in matches_for_this_gpu:
                    all_matched_gpus.append((gpu, brand, model_number, vram, model_number))

    if debug:
        print("\nAll matched GPUs:", all_matched_gpus)

    if not all_matched_gpus:
        return "Unknown", None, None, None, None, 0

    # If we found multiple different GPUs, return Multi
    if len(set(gpu[0] for gpu in all_matched_gpus)) > 1:
        matched_models = [gpu[2] for gpu in all_matched_gpus]
        return "Multi", None, matched_models, None, matched_models[0], len(all_matched_gpus)

    # If all matches are for the same GPU, return that one
    return all_matched_gpus[0][0], all_matched_gpus[0][1], all_matched_gpus[0][2], all_matched_gpus[0][3], all_matched_gpus[0][4], 1

def fetch_page(page: int = 1) -> dict:
    """Fetch a single page of GPU listings"""
    params = API["params"].copy()
    params["page"] = page
    try:
        response = requests.get(API["base_url"], params=params, timeout=30)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching page {page}: {e}")
        return None

def fetch_description(url: str) -> str:
    """Fetch and parse item description"""
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        about_section = soup.find('section', class_='about-section')
        if about_section:
            # Get text while preserving spaces and newlines
            text = about_section.get_text(separator=' ', strip=True)
            # Replace multiple spaces with single space
            text = re.sub(r'\s+', ' ', text)
            return text
        return ""
    except requests.RequestException:
        return ""

def process_listings(items: list, gpu_models: list, blacklist: dict, whitelist: dict, verbose: bool = False) -> pd.DataFrame:
    """Process raw listings into structured data with progress tracking"""
    processed_items = []
    skipped_count = 0
    skip_patterns = [re.compile(rf'\b{re.escape(term)}\b', re.IGNORECASE) for term in SKIP_TERMS]

    pbar = tqdm(items, desc="Processing listings")
    unknown_count = 0

    for item in pbar:
        heading = item.get('heading', '')
        ad_id = str(item.get('id', ''))

        # If whitelist exists, only process whitelisted items
        if whitelist['patterns'] or whitelist['ids']:
            if ad_id not in whitelist['ids'] and \
               not any(pattern in heading.lower() for pattern in whitelist['patterns']):
                continue
            elif verbose:
                print(f"\nProcessing whitelisted item {ad_id}:")
                print(f"Title: {heading}")
        else:
            # If no whitelist, apply blacklist and skip terms
            if ad_id in blacklist['ids'] or \
               any(pattern in heading.lower() for pattern in blacklist['patterns']):
                continue

            # Improved skip term matching with whole-word check
            if any(pattern.search(heading) for pattern in skip_patterns):
                if verbose:
                    print(f"Skipping item {ad_id} containing: {heading}")
                skipped_count += 1
                continue

        # Extract GPU info from title
        model, brand, model_number, vram, matched_number, match_count = match_gpu_model(heading, gpu_models, debug=verbose)

        if verbose:
            print(f"Matched model: {model}")
            if brand:
                print(f"Brand: {brand}")
            if model_number:
                print(f"Model number: {model_number}")
            if vram:
                print(f"VRAM: {vram}GB")
            print("-" * 80)

        # Track if we'll need to fetch description
        if model == "Unknown":
            unknown_count += 1

        processed_items.append({
            "heading": item.get('heading', ''),
            "price": item.get("price", {}).get("amount", "N/A"),
            "model": model,
            "brand": brand,
            "model_number": model_number,
            "vram": vram,
            "matched_number": matched_number,
            "match_count": match_count,
            "location": item.get("location", "N/A"),
            "ad_id": ad_id,
            "canonical_url": item.get("canonical_url", "")
        })

    print(f"\nSkipped {skipped_count} items containing: {', '.join(SKIP_TERMS)}")

    # Fetch descriptions for unknowns if needed
    if unknown_count > 0:
        rate_limit = RateLimiter(API["rate_limit"])
        print(f"\nFetching descriptions for {unknown_count} unmatched items...")
        desc_pbar = tqdm(processed_items, desc="Fetching descriptions")

        for item in desc_pbar:
            if item["model"] == "Unknown":
                desc_pbar.set_postfix_str(f"Processing: {item['ad_id']}...")
                rate_limit()
                description = fetch_description(item["canonical_url"])
                if description:
                    if verbose:
                        print(f"\nTrying to match from description for {item['ad_id']}:")
                        print(f"Description: {description[:200]}...")

                    model, brand, model_number, vram, matched_number, match_count = match_gpu_model(
                        description, gpu_models, debug=verbose
                    )

                    if model != "Unknown":
                        item.update({
                            "model": model,
                            "brand": brand,
                            "model_number": model_number,
                            "vram": vram,
                            "matched_number": matched_number,
                            "match_count": match_count
                        })

    return pd.DataFrame(processed_items)

def main():
    parser = argparse.ArgumentParser(description="Fetch and process GPU listings from Finn.no")
    parser.add_argument("-f", "--file", type=str, help="Process existing CSV file")
    parser.add_argument("-b", "--blacklist", type=Path, default=BLACKLIST_FILE, help="Blacklist file path")
    parser.add_argument("-w", "--whitelist", type=Path, help="Whitelist file path")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")
    args = parser.parse_args()

    # Load GPU models and filter lists
    gpu_models = load_gpu_models()
    blacklist = load_filter_list(args.blacklist, "blacklist")
    whitelist = load_filter_list(args.whitelist, "whitelist") if args.whitelist else {'patterns': [], 'ids': []}

    if args.verbose:
        print("\nLoaded configuration:")
        if whitelist['ids']:
            print(f"Whitelist IDs: {', '.join(whitelist['ids'])}")
        if whitelist['patterns']:
            print(f"Whitelist patterns: {', '.join(whitelist['patterns'])}")
        print(f"Skip terms: {', '.join(SKIP_TERMS)}")
        print("-" * 80)

    # Set up rate limiter
    rate_limit = RateLimiter(API["rate_limit"])

    if args.file:
        # Process existing file
        try:
            df = pd.read_csv(args.file)
        except Exception as e:
            print(f"Error reading file: {e}")
            return
    else:
        # Fetch new listings
        all_items = []
        page = 1
        with tqdm(desc="Fetching pages") as pbar:
            while True:
                rate_limit()
                data = fetch_page(page)
                if not data:
                    break

                items = data.get("docs", [])
                if not items:
                    break

                all_items.extend(items)
                page += 1
                pbar.update(1)

        # Process fetched listings
        df = process_listings(all_items, gpu_models, blacklist, whitelist, verbose=args.verbose)

    # Save results
    output_path = OUTPUT_DIR / OUTPUT_FORMAT.format(date=datetime.now().strftime("%Y-%m-%d"))
    df.to_csv(output_path, index=False)
    print(f"\nData saved to {output_path}")

    # Print statistics
    total = len(df)
    if "model" in df.columns:
        matched = len(df[~df['model'].isin(['Unknown', 'Multi'])])
        print(f"\nStatistics:")
        print(f"Total listings: {total}")
        print(f"Successfully matched: {matched} ({matched/total:.1%})")

        if args.verbose:
            print("\nModel distribution:")
            print(df['model'].value_counts())
            print("\nFinal results by ID:")
            for _, row in df.iterrows():
                print(f"\nAd ID: {row['ad_id']}")
                print(f"Title: {row['heading']}")
                print(f"Model: {row['model']}")
                print(f"Price: {row['price']}")
                print(f"URL: {row['canonical_url']}")
    else:
        print(f"\nWarning: 'model' column not found in DataFrame")
        print(f"Available columns: {', '.join(df.columns)}")

if __name__ == "__main__":
    main()
