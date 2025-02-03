from pathlib import Path

# Base paths
BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
LOG_DIR = BASE_DIR / "logs"

# Ensure directories exist
DATA_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)

# API settings
API = {
    "base_url": "https://www.finn.no/api/search-qf",
    "rate_limit": 4,  # requests per second
    "params": {
        "searchkey": "SEARCH_ID_BAP_COMMON",
        "product_category": ["2.93.3215.8368", "2.93.3215.46", "2.93.3215.44"],
        "q": "skjermkort or gpu",
        "price_from": 1000,
        "price_to": 8000,
        "trade_type": "1",
        "vertical": "bap"
    }
}

# File paths
MODELS_FILE = BASE_DIR / "gpus.json"
BLACKLIST_FILE = BASE_DIR / "blacklist.txt"
WHITELIST_FILE = BASE_DIR / "whitelist.txt"

# Listing processing
SKIP_TERMS = ['pc', 'stasjonær', 'mining', 'mac', 'laptop', 'dell', 'gamingpoint', 'datamaskin', 'server', 'windows', 'lenovo', 'desktop', 'kjøler']

# Output settings
OUTPUT_DIR = Path("/var/www/finngpu/data")
OUTPUT_FORMAT = "finn_gpu_listings_{date}.csv"
