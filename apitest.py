import requests
import json
from pprint import pprint

def analyze_api_structure(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        print("Top-level structure:")
        pprint(list(data.keys()))

        if 'docs' in data:
            print("\nStructure of the first item in 'docs':")
            pprint(list(data['docs'][0].keys()))

            print("\nSample data from the first item:")
            for key, value in data['docs'][0].items():
                print(f"{key}: {value[:100] if isinstance(value, str) else value}")

        print("\nTotal number of items:", len(data.get('docs', [])))

    except requests.exceptions.RequestException as e:
        print(f"Error occurred while fetching data: {e}")
    except json.JSONDecodeError:
        print("Error occurred while parsing JSON response")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    url = "https://www.finn.no/api/search-qf?searchkey=SEARCH_ID_BAP_COMMON&product_category=2.93.3215.46&product_category=2.93.3215.8368&q=skjermkort&trade_type=1&vertical=bap"
    analyze_api_structure(url)
