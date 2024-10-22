import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm
import json
import re
import argparse
import time
from collections import deque
from datetime import datetime

class RateLimiter:
    def __init__(self, max_calls, period):
        self.max_calls = max_calls
        self.period = period
        self.calls = deque()

    def __call__(self):
        now = time.time()
        while self.calls and self.calls[0] <= now - self.period:
            self.calls.popleft()
        if len(self.calls) >= self.max_calls:
            sleep_time = self.calls[0] - (now - self.period)
            time.sleep(sleep_time)
        self.calls.append(time.time())

# Rate limiter: 4 calls per second
rate_limiter = RateLimiter(4, 1)

def load_gpu_models():
    with open('gpus.json', 'r') as f:
        return json.load(f)

def load_blacklist(filename):
    blacklist = {'patterns': [], 'ids': []}
    try:
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    # If the line contains only digits, treat it as an ID
                    if line.isdigit():
                        blacklist['ids'].append(line)
                    else:
                        blacklist['patterns'].append(line.lower())
    except FileNotFoundError:
        print(f"Blacklist file {filename} not found. Proceeding without a blacklist.")
    return blacklist

def is_blacklisted(item, blacklist):
    # Check ad ID
    ad_id = str(item.get('id', ''))
    if ad_id in blacklist['ids']:
        return True

    # Check title against patterns
    heading = item.get('heading', '').lower()
    return any(pattern in heading for pattern in blacklist['patterns'])


def extract_model_info(text):
    text_lower = text.lower()
    brand = None
    if 'nvidia' in text_lower or 'geforce' in text_lower or 'gtx' in text_lower or 'rtx' in text_lower:
        brand = 'NVIDIA'
    elif 'amd' in text_lower or 'radeon' in text_lower or 'rx' in text_lower:
        brand = 'AMD'

    model_pattern = r'\b(gtx|rtx|rx)?\s*(\d{3,4})\s*(ti|xt|super|s)?\b'
    model_matches = re.findall(model_pattern, text_lower)

    model_numbers = []
    for prefix, number, suffix in model_matches:
        if suffix == 's':
            suffix = 'super'
        if not prefix:
            prefix = ''  # Set prefix to empty string if it's None
        model = f"{prefix} {number} {suffix}".strip()
        model = ' '.join(model.split())
        if model:
            model_numbers.append(model)

        # Infer brand from prefix if not already set
        if not brand:
            if prefix in ['gtx', 'rtx']:
                brand = 'NVIDIA'
            elif prefix == 'rx':
                brand = 'AMD'

    vram = re.search(r'(\d+)\s*gb', text_lower)
    vram = vram.group(1) if vram else None

    return brand, model_numbers, vram

def match_gpu_model(title, gpu_models):
    brand, model_numbers, vram = extract_model_info(title)

    if brand is None and model_numbers is None and vram is None:
        return "Skipped", None, None, None, None, 0

    if not model_numbers:
        return "Unknown", brand, None, vram, None, 0

    matches = []
    for gpu in reversed(gpu_models):
        gpu_lower = gpu.lower()
        for model_number in model_numbers:
            model_lower = model_number.lower()
            if model_lower in gpu_lower:
                # Check for exact match or correct suffix handling
                is_match = re.search(rf'\b{re.escape(model_lower)}\b', gpu_lower)

                # Handle suffix matching
                if ' ti' in gpu_lower:
                    is_match = is_match and ' ti' in model_lower
                elif ' super' in gpu_lower:
                    is_match = is_match and ' super' in model_lower
                elif ' xt' in gpu_lower:
                    is_match = is_match and ' xt' in model_lower

                if is_match:
                    # Infer brand if not explicitly mentioned
                    inferred_brand = brand
                    if not inferred_brand:
                        if 'geforce' in gpu_lower or 'gtx' in gpu_lower or 'rtx' in gpu_lower:
                            inferred_brand = 'NVIDIA'
                        elif 'radeon' in gpu_lower or 'rx' in gpu_lower:
                            inferred_brand = 'AMD'

                    # Check if the brand matches or wasn't specified
                    if not brand or (inferred_brand == brand):
                        if vram:
                            vram_match = re.search(r'(\d+)\s*gb', gpu_lower)
                            if vram_match and int(vram_match.group(1)) == int(vram):
                                matches.append((gpu, inferred_brand, model_number, vram, model_number))
                        else:
                            matches.append((gpu, inferred_brand, model_number, vram, model_number))

    if len(matches) > 1:
        return "Multi", brand, [m[2] for m in matches], vram, [m[4] for m in matches], len(matches)
    elif len(matches) == 1:
        return matches[0] + (1,)
    else:
        return "Unknown", brand, model_numbers[0] if model_numbers else None, vram, None, 0

def fetch_data(page=1):
    rate_limiter()

    base_url = "https://www.finn.no/api/search-qf"
    params = {
        "searchkey": "SEARCH_ID_BAP_COMMON",
        "product_category": ["2.93.3215.8368", "2.93.3215.46", "2.93.3215.44"],
        "q": "skjermkort",
        "price_from": 1000,
        "price_to": 8000,
        "trade_type": "1",
        "vertical": "bap",
        "page": page
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"An error occurred while fetching data: {e}")
        return None

def extract_info(item, gpu_models):
    heading = item.get("heading", "")
    model, brand, model_number, vram, matched_model_number, match_count = match_gpu_model(heading, gpu_models)
    return {
        "heading": heading,
        "price": item.get("price", {}).get("amount", "N/A"),
        "model": model,
        "extracted_brand": brand,
        "extracted_model": model_number,
        "extracted_vram": vram,
        "matched_model_number": matched_model_number,
        "match_count": match_count,
        "location": item.get("location", "N/A"),
        "ad_id": item.get("id", ""),
        "canonical_url": item.get("canonical_url", "")
    }

def fetch_and_process_data(gpu_models, blacklist):
    all_items = []
    page = 1
    total_pages = 1  # We'll update this after the first request

    with tqdm(total=None, desc="Fetching pages") as pbar:
        while page <= total_pages:
            rate_limiter()
            data = fetch_data(page)
            if not data:
                break

            if page == 1:
                total_pages = data.get("metadata", {}).get("paging", {}).get("last", 1)
                pbar.total = total_pages

            items = data.get("docs", [])
            processed_items = [extract_info(item, gpu_models) for item in items if not is_blacklisted(item, blacklist)]
            all_items.extend(processed_items)

            page += 1
            pbar.update(1)

            if not items:
                break  # No more results

    return pd.DataFrame(all_items)

def fetch_and_parse_description(url):
    rate_limiter()  # Apply rate limiting
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        about_section = soup.find('section', class_='about-section')
        if about_section:
            return about_section.get_text(strip=True)
        return ""
    except requests.RequestException as e:
        print(f"An error occurred while fetching description for {url}: {e}")
        return ""

def process_unknown_gpus(df, gpu_models):
    unknown_mask = (df['model'] == 'Unknown')
    unknown_df = df[unknown_mask]

    print(f"Processing {len(unknown_df)} GPUs without extracted model")

    tqdm.pandas(desc="Processing GPUs without extracted model")

    def process_row(row):
        description = fetch_and_parse_description(row['canonical_url'])
        old_model = row['model']
        model, brand, model_number, vram, matched_model_number, match_count = match_gpu_model(description, gpu_models)
        if model != 'Unknown' and model != 'Skipped':
            row['model'] = model
            row['extracted_brand'] = brand
            row['extracted_model'] = model_number
            row['extracted_vram'] = vram
            row['matched_model_number'] = matched_model_number
            row['match_count'] = match_count
        return row

    updated_unknown_df = unknown_df.progress_apply(process_row, axis=1)
    df.update(updated_unknown_df)

    successfully_matched = ((updated_unknown_df['model'] != 'Unknown') & (updated_unknown_df['model'] != 'Skipped')).sum()
    print(f"Successfully matched {successfully_matched} out of {len(unknown_df)} previously unknown GPUs")

    return df

def process_existing_data(filename, gpu_models, blacklist):
    df = pd.read_csv(filename)
    tqdm.pandas(desc="Processing existing data")
    df[['model', 'extracted_brand', 'extracted_model', 'extracted_vram', 'matched_model_number', 'match_count']] = df['heading'].progress_apply(lambda x: pd.Series(match_gpu_model(x, gpu_models)))

    # Apply blacklist to existing data
    df['is_blacklisted'] = df.apply(lambda row: is_blacklisted({'heading': row['heading'], 'seller': {'name': row['seller']}}, blacklist), axis=1)
    df = df[~df['is_blacklisted']].drop('is_blacklisted', axis=1)

    return df

def reorder_csv_columns(df):
    columns = df.columns.tolist()
    columns.append(columns.pop(columns.index('canonical_url')))
    return df[columns]

def main():
    parser = argparse.ArgumentParser(description="GPU listing processor")
    parser.add_argument("-f", "--file", type=str, help="Path to existing CSV file to process")
    parser.add_argument("-b", "--blacklist", type=str, default="blacklist.txt", help="Path to blacklist file")
    args = parser.parse_args()

    gpu_models = load_gpu_models()
    blacklist = load_blacklist(args.blacklist)

    if args.file:
        df = process_existing_data(args.file, gpu_models, blacklist)
        output_filename = args.file
    else:
        df = fetch_and_process_data(gpu_models, blacklist)
        current_date = datetime.now().strftime("%Y-%m-%d")
        output_filename = f"finn_gpu_listings_{current_date}.csv"

    initial_total = len(df)
    df = df[df['model'] != 'Skipped']  # Remove skipped GPUs
    initial_known_count = df['model'].value_counts().drop(['Unknown'], errors='ignore').sum()
    print(f"Initially matched models: {initial_known_count} out of {len(df)}")

    # Process GPUs without extracted model
    df = process_unknown_gpus(df, gpu_models)

    df = reorder_csv_columns(df)
    df.to_csv(output_filename, index=False)
    print(f"Data saved to {output_filename}")

    final_known_count = df['model'].value_counts().drop(['Unknown'], errors='ignore').sum()
    total_models = len(df)

    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    print(df.head())
    print(f"Final successfully matched models: {final_known_count} out of {total_models} ({final_known_count/total_models:.2%})")
    print(f"Skipped items removed: {initial_total - len(df)}")
    print(f"Improvement: {final_known_count - initial_known_count} additional models matched")

if __name__ == "__main__":
    main()
