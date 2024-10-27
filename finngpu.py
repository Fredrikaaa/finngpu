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

def match_gpu_model(text: str, gpu_models: list) -> tuple:
    """Match GPU model from text with improved pattern matching"""
    text = text.lower()

    # Main pattern for GPU model detection
    pattern = r'\b(?:(?:geforce|nvidia|rtx|gtx|radeon|rx)\s*)?(\d{3,4})\s*(ti|xt|super)?\s*(?:(\d+)\s*gb)?\b'
    matches = list(re.finditer(pattern, text))

    if not matches:
        return "Unknown", None, None, None, None, 0

    # Extract info from best match
    match = matches[0]  # Take first match as primary
    number = match.group(1)
    suffix = match.group(2) or ''
    vram = match.group(3)

    # Determine brand from text
    prefix = text[match.start():match.start(1)].strip()
    brand = 'NVIDIA' if any(x in prefix for x in ['geforce', 'nvidia', 'rtx', 'gtx']) else \
           'AMD' if any(x in prefix for x in ['radeon', 'rx']) else None

    model_number = f"{number} {suffix}".strip()

    # Find matching models
    matches = []
    for gpu in gpu_models:
        gpu_lower = gpu.lower()

        # Skip if brands don't match (when brand is known)
        if brand:
            gpu_brand = 'NVIDIA' if any(x in gpu_lower for x in ['geforce', 'rtx', 'gtx']) else \
                       'AMD' if any(x in gpu_lower for x in ['radeon', 'rx']) else None
            if gpu_brand and brand != gpu_brand:
                continue

        # Check model number match
        if re.search(rf'\b{model_number}\b', gpu_lower):
            # Verify VRAM if specified
            if vram:
                vram_match = re.search(rf'{vram}\s*gb', gpu_lower)
                if not vram_match:
                    continue
            matches.append(gpu)

    if not matches:
        return "Unknown", brand, model_number, vram, model_number, 0
    if len(matches) == 1:
        return matches[0], brand, model_number, vram, model_number, 1
    return "Multi", brand, model_number, vram, model_number, len(matches)

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
        return about_section.get_text(strip=True) if about_section else ""
    except requests.RequestException:
        return ""

def process_listings(items: list, gpu_models: list, blacklist: dict, whitelist: dict) -> pd.DataFrame:
    """Process raw listings into structured data"""
    processed_items = []

    for item in items:
        # Skip if blacklisted
        if str(item.get('id', '')) in blacklist['ids'] or \
           any(pattern in item.get('heading', '').lower() for pattern in blacklist['patterns']):
            continue

        # Skip if not whitelisted (when whitelist is used)
        if whitelist['patterns'] or whitelist['ids']:
            if str(item.get('id', '')) not in whitelist['ids'] and \
               not any(pattern in item.get('heading', '').lower() for pattern in whitelist['patterns']):
                continue

        # Extract GPU info
        heading = item.get('heading', '')
        model, brand, model_number, vram, matched_number, match_count = match_gpu_model(heading, gpu_models)

        # If no match found in title, try description
        if model == "Unknown":
            description = fetch_description(item.get('canonical_url', ''))
            if description:
                model, brand, model_number, vram, matched_number, match_count = match_gpu_model(description, gpu_models)

        processed_items.append({
            "heading": heading,
            "price": item.get("price", {}).get("amount", "N/A"),
            "model": model,
            "extracted_brand": brand,
            "extracted_model": model_number,
            "extracted_vram": vram,
            "matched_model_number": matched_number,
            "match_count": match_count,
            "location": item.get("location", "N/A"),
            "ad_id": item.get("id", ""),
            "canonical_url": item.get("canonical_url", "")
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

    # Set up rate limiter
    rate_limit = RateLimiter(API["rate_limit"])

    if args.file:
        # Process existing file
        df = pd.read_csv(args.file)
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
        df = process_listings(all_items, gpu_models, blacklist, whitelist)

    # Save results
    output_path = DATA_DIR / OUTPUT_FORMAT.format(date=datetime.now().strftime("%Y-%m-%d"))
    df.to_csv(output_path, index=False)
    print(f"\nData saved to {output_path}")

    # Print statistics
    total = len(df)
    matched = df['model'].value_counts().drop(['Unknown', 'Multi'], errors='ignore').sum()
    print(f"\nStatistics:")
    print(f"Total listings: {total}")
    print(f"Successfully matched: {matched} ({matched/total:.1%})")

if __name__ == "__main__":
    main()
