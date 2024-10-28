import random
from finngpu import fetch_page, match_gpu_model, load_gpu_models, fetch_description
from config import SKIP_TERMS
import json
import time
from pathlib import Path
import pickle
import sys
import threading
from queue import Queue, Empty
from collections import deque
from tqdm import tqdm

def escape_string(s):
    """Escape a string for use in Python string literal"""
    return (s.replace('\\', '\\\\')  # Must be first to avoid double-escaping
            .replace('"', '\\"')
            .replace("'", "\\'")
            .replace('\n', '\\n')
            .replace('\r', '\\r')
            .replace('\t', '\\t'))

class DescriptionFetcher:
    def __init__(self, max_workers=2):
        self.queue = Queue()
        self.results = {}
        self.active = True
        self.workers = []

        # Start worker threads
        for _ in range(max_workers):
            worker = threading.Thread(target=self._worker)
            worker.daemon = True
            worker.start()
            self.workers.append(worker)

    def _worker(self):
        """Worker thread that fetches descriptions"""
        while self.active:
            try:
                ad_id, url = self.queue.get(timeout=1)
                if not url in self.results:
                    description = fetch_description(url)
                    self.results[url] = description
                    time.sleep(0.25)  # Be nice to the server
                self.queue.task_done()
            except Empty:
                continue

    def add_listing(self, ad_id, url):
        """Add a listing to the queue for processing"""
        self.queue.put((ad_id, url))

    def get_description(self, url):
        """Get a description if it's ready, otherwise return None"""
        return self.results.get(url)

    def shutdown(self):
        """Shutdown the fetcher and wait for pending work to complete"""
        self.active = False
        for worker in self.workers:
            worker.join()

class TestSetGenerator:
    def __init__(self):
        self.gpu_models = load_gpu_models()
        self.progress_file = Path("test_set_progress.pkl")
        self.processed_ids = set()
        self.test_cases = []
        self.archived_listings = []
        self.description_fetcher = DescriptionFetcher()

    def load_progress(self):
        """Load previous progress if it exists"""
        if self.progress_file.exists():
            try:
                with open(self.progress_file, 'rb') as f:
                    data = pickle.load(f)
                self.processed_ids = data['processed_ids']
                self.test_cases = data['test_cases']
                self.archived_listings = data['archived_listings']
                return True
            except Exception as e:
                print(f"Error loading progress file: {e}")
                return False
        return False

    def save_progress(self):
        """Save current progress"""
        with open(self.progress_file, 'wb') as f:
            pickle.dump({
                'processed_ids': self.processed_ids,
                'test_cases': self.test_cases,
                'archived_listings': self.archived_listings
            }, f)

    def save_test_set(self):
        """Generate and save the test_set.py file"""
        output = "# Test set for GPU matching validation\n"
        output += "# Format: (ad_id, expected_model, listing_title)\n"
        output += "# Including listing titles to make manual verification easier\n"
        output += "test_cases = [\n"

        # Group test cases by category
        categories = ["NVIDIA", "AMD", "Multi", "Unknown"]

        for category in categories:
            # Filter test cases for this category
            category_cases = [
                case for case in self.test_cases
                if determine_category(case[1]) == category
            ]

            if category_cases:
                output += f"\n    # {category} GPUs\n"
                for ad_id, model, title in sorted(category_cases):
                    output += f'    ("{ad_id}", "{escape_string(model)}", "{escape_string(title)}"),\n'

        output += "]\n\n"

        # Add archived listings data
        output += "# Archived listing data for future testing\n"
        output += "archived_listings = {\n"
        for listing in self.archived_listings:
            output += f"    '{listing['id']}': {{\n"
            output += f"        'heading': '''{escape_string(listing['heading'])}''',\n"
            output += f"        'description': '''{escape_string(listing['description'])}''',\n"
            output += f"        'url': '{escape_string(listing['url'])}'\n"
            output += "    },\n"
        output += "}\n"

        # Add mock functions for testing
        output += """
# Mock functions for testing
def mock_fetch_page(page):
    \"\"\"Mock version of fetch_page for testing\"\"\"
    if page == 1:
        return {
            'docs': [
                {
                    'id': ad_id,
                    'heading': data['heading'],
                    'canonical_url': data['url']
                }
                for ad_id, data in archived_listings.items()
            ]
        }
    return {'docs': []}

def mock_fetch_description(url):
    \"\"\"Mock version of fetch_description for testing\"\"\"
    for listing in archived_listings.values():
        if listing['url'] == url:
            return listing['description']
    return ""
"""

        # Write to file
        with open("test_set.py", "w", encoding="utf-8") as f:
            f.write(output)

    def process_listings(self, listings):
        """Process listings with background description fetching"""
        # Create a deque of unprocessed listings
        remaining_listings = deque(
            listing for listing in listings
            if listing.get('id', '') not in self.processed_ids
        )

        # Calculate progress numbers
        total = len(remaining_listings) + len(self.processed_ids)  # Total including already processed
        current = len(self.processed_ids)  # Start from number already processed

        # Queue up initial batch of descriptions
        lookahead = 5  # Number of descriptions to pre-fetch
        for i in range(min(lookahead, len(remaining_listings))):
            listing = remaining_listings[i]
            self.description_fetcher.add_listing(
                listing.get('id', ''),
                listing.get('canonical_url', '')
            )

        print("\nProcessing listings...")
        print("Controls:")
        print("- Press Enter to confirm suggested model")
        print("- Type a new model name to correct")
        print("- Type 'skip' to skip this listing")
        print("- Type 'q' to save and quit")
        print("\nProgress will be automatically saved after each listing")

        try:
            while remaining_listings:
                item = remaining_listings.popleft()
                ad_id = item.get('id', '')
                title = item.get('heading', '')
                url = item.get('canonical_url', '')

                # Queue next description if available
                if len(remaining_listings) >= lookahead:
                    next_item = remaining_listings[lookahead-1]
                    self.description_fetcher.add_listing(
                        next_item.get('id', ''),
                        next_item.get('canonical_url', '')
                    )

                # Get suggested model
                suggested_model, _, _, _, _, _ = match_gpu_model(title, self.gpu_models)

                # Clear previous lines and print current listing with enhanced formatting
                print("\n" + "="*80)
                print(f"Progress: {current}/{total} listings processed")
                print(f"Ad ID: {ad_id}")
                if url:
                    print(f"URL: {url}")
                print("-" * 80)
                print(f"TITLE:")
                print(f">>> {title}")
                print("-" * 80)
                print(f"SUGGESTED MODEL:")
                print(f">>> {suggested_model}")
                print("-" * 80)

                # Get user input
                user_input = input("Press enter to confirm or type out the correct model name. Write 'skip' to skip or 'q' to quit: ").strip()

                if user_input.lower() == 'q':
                    print("\nSaving progress and exiting...")
                    self.save_progress()
                    return True

                # Process the input
                if user_input.lower() != 'skip':
                    final_model = user_input if user_input else suggested_model

                    # Try to get pre-fetched description or fetch if not ready
                    description = self.description_fetcher.get_description(url)
                    if description is None:
                        print(f"Fetching description...")
                        description = fetch_description(url)
                        time.sleep(0.25)

                    # Archive the listing data
                    archived_listing = {
                        'id': ad_id,
                        'heading': title,
                        'description': description,
                        'url': url
                    }
                    self.archived_listings.append(archived_listing)

                    # Add to test cases
                    self.test_cases.append((ad_id, final_model, title))

                # Mark as processed and update progress
                self.processed_ids.add(ad_id)
                self.save_progress()
                current += 1

        except KeyboardInterrupt:
            print("\nInterrupted by user. Progress has been saved.")
            return True
        finally:
            # Shutdown the description fetcher
            self.description_fetcher.shutdown()

        return False

    def __del__(self):
        """Ensure description fetcher is shut down"""
        if hasattr(self, 'description_fetcher'):
            self.description_fetcher.shutdown()

def should_skip_listing(title):
    """Check if listing should be skipped based on title"""
    return any(term.lower() in title.lower() for term in SKIP_TERMS)

def determine_category(model):
    """Determine the category for a given model"""
    if model == "Multi":
        return "Multi"
    elif model == "Unknown":
        return "Unknown"
    elif any(brand in model for brand in ["GeForce", "GTX", "RTX"]):
        return "NVIDIA"
    elif any(brand in model for brand in ["Radeon", "RX"]):
        return "AMD"
    else:
        return "Unknown"

def main():
    generator = TestSetGenerator()

    # Try to load previous progress
    if generator.load_progress():
        print("Loaded previous progress")
        print(f"Previously processed: {len(generator.processed_ids)} listings")
        print(f"Current test cases: {len(generator.test_cases)}")
        continue_previous = input("Continue from previous session? (Y/n): ").strip().lower()
        if continue_previous == 'n':
            print("Starting fresh...")
            generator = TestSetGenerator()

    # Fetch all listings from all pages
    print("\nFetching listings...")
    all_items = []
    page = 1
    with tqdm(desc="Fetching pages") as pbar:
        while True:
            data = fetch_page(page)
            if not data:
                break

            items = data.get("docs", [])
            if not items:
                break

            all_items.extend(items)
            page += 1
            pbar.update(1)

    # Filter out listings with skip terms
    filtered_listings = [
        listing for listing in all_items
        if not should_skip_listing(listing.get('heading', ''))
    ]

    print(f"Found {len(all_items)} total listings")
    print(f"Filtered to {len(filtered_listings)} listings after removing skip terms")

    # Randomly select 50% of remaining listings
    sample_size = len(filtered_listings) // 2
    selected_listings = random.sample(filtered_listings, sample_size)

    # Sort by ID to make review easier
    selected_listings.sort(key=lambda x: x.get('id', ''))

    # Process listings
    quit_early = generator.process_listings(selected_listings)

    # Generate final output
    generator.save_test_set()

    print("\nTest set has been generated and saved to test_set.py")
    print(f"Total test cases: {len(generator.test_cases)}")
    print("File includes:")
    print("- Test cases grouped by category")
    print("- Archived listing data (titles and descriptions)")
    print("- Mock functions for testing")

    if not quit_early:
        # Clean up progress file if completed successfully
        generator.progress_file.unlink(missing_ok=True)

if __name__ == "__main__":
    main()
