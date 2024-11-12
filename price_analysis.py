import pandas as pd
import argparse
import re
import glob
import os
from datetime import datetime

def parse_args():
    parser = argparse.ArgumentParser(
        description="Analyze GPU listings and find the best price-to-performance ratios.",
        epilog="Example usage:\n"
               "  %(prog)s -p performance.csv                                    # Use latest listings\n"
               "  %(prog)s -p performance.csv --brand nvidia                     # Filter by brand\n"
               "  %(prog)s -p performance.csv --max-price 5000 --min-fps 100    # Filter by price and performance\n",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("-f", "--file",
                       help="Path to specific CSV file containing GPU listings. If not provided, uses most recent finn_gpu_listings_*.csv")
    parser.add_argument("-p", "--performance", required=True,
                       help="Path to the CSV file containing 1440p performance data")
    parser.add_argument("-c", "--csv", dest="output_csv", metavar="OUTPUT_FILE",
                       help="Output results to a CSV file instead of console")

    # Add new filtering arguments
    filter_group = parser.add_argument_group('filtering options')
    filter_group.add_argument("--brand",
                            help="Filter by brand (e.g., 'nvidia' or 'amd')",
                            type=str.lower)
    filter_group.add_argument("--min-price",
                            help="Minimum price to include",
                            type=float)
    filter_group.add_argument("--max-price",
                            help="Maximum price to include",
                            type=float)
    filter_group.add_argument("--min-fps",
                            help="Minimum 1440p FPS to include",
                            type=float)
    filter_group.add_argument("--max-fps",
                            help="Maximum 1440p FPS to include",
                            type=float)
    filter_group.add_argument("--exclude-models",
                            help="Comma-separated list of model patterns to exclude (e.g., '3060,6700')",
                            type=str)
    return parser.parse_args()

def find_latest_gpu_listings():
    # Find all files matching the pattern
    files = glob.glob("finn_gpu_listings_*.csv")

    if not files:
        raise FileNotFoundError("No GPU listing files found matching pattern 'finn_gpu_listings_*.csv'")

    # Extract dates from filenames and pair with filenames
    dated_files = []
    for file in files:
        try:
            date_match = re.search(r'finn_gpu_listings_(\d{4}-\d{2}-\d{2})\.csv', file)
            if date_match:
                date_str = date_match.group(1)
                file_date = datetime.strptime(date_str, '%Y-%m-%d')
                dated_files.append((file_date, file))
        except ValueError:
            continue

    if not dated_files:
        raise ValueError("No valid dated GPU listing files found")

    # Sort by date and get the most recent file
    latest_file = sorted(dated_files, key=lambda x: x[0], reverse=True)[0][1]
    print(f"Using most recent GPU listings file: {latest_file}")
    return latest_file

def parse_gpu_listings(filename):
    # Read the CSV file
    df = pd.read_csv(filename)

    # Filter out 'Unknown' and 'Multi' models
    df = df[~df['model'].isin(['Unknown', 'Multi'])]

    # Find the index of the minimum price for each model
    idx = df.groupby('model')['price'].idxmin()

    # Select the rows with the minimum price for each model
    cheapest_prices = df.loc[idx, ['model', 'price', 'canonical_url']].reset_index(drop=True)

    return cheapest_prices

def apply_filters(df, args):
    """Apply filters based on command line arguments."""
    filtered_df = df.copy()

    if args.brand:
        # Convert model names to lowercase for case-insensitive comparison
        filtered_df = filtered_df[filtered_df['model'].str.lower().str.contains(args.brand)]

    if args.min_price is not None:
        filtered_df = filtered_df[filtered_df['price'] >= args.min_price]

    if args.max_price is not None:
        filtered_df = filtered_df[filtered_df['price'] <= args.max_price]

    if args.min_fps is not None:
        filtered_df = filtered_df[filtered_df['1440p Ultra FPS'] >= args.min_fps]

    if args.max_fps is not None:
        filtered_df = filtered_df[filtered_df['1440p Ultra FPS'] <= args.max_fps]

    if args.exclude_models:
        exclude_patterns = [pattern.strip().lower() for pattern in args.exclude_models.split(',')]
        # Create a boolean mask for models that don't match any exclude pattern
        mask = ~filtered_df['model'].str.lower().str.contains('|'.join(exclude_patterns))
        filtered_df = filtered_df[mask]

    return filtered_df

def load_and_process_data(listings_file, performance_file, args):
    # Get the cheapest price for each GPU model
    cheapest_df = parse_gpu_listings(listings_file)

    # Load the 1440p performance data
    performance_df = pd.read_csv(performance_file)

    # Merge the dataframes based on exact model names
    merged_df = pd.merge(cheapest_df, performance_df,
                        left_on='model',
                        right_on='Graphics Card',
                        how='inner')

    # Print unmatched models for debugging
    unmatched_models = cheapest_df[~cheapest_df['model'].isin(merged_df['model'])]
    if not unmatched_models.empty:
        print("\nWarning: The following models from listings didn't match performance data:")
        for model in unmatched_models['model']:
            print(f"- {model}")

    # Calculate price per FPS and round to 1 decimal place
    merged_df['Price per FPS'] = (merged_df['price'] / merged_df['1440p Ultra FPS']).round(1)

    # Apply filters
    filtered_df = apply_filters(merged_df, args)

    # Sort by Price per FPS
    sorted_df = filtered_df.sort_values('Price per FPS')

    # Clean up the result
    result_df = sorted_df[['model', 'price', '1440p Ultra FPS', 'Price per FPS', 'canonical_url']]

    return result_df

def display_results(df, output_csv=None):
    if df.empty:
        print("\nNo results found matching the specified filters.")
        return

    if output_csv:
        # Output to CSV file
        df.to_csv(output_csv, index=False)
        print(f"Results have been saved to {output_csv}")
    else:
        # Print the table header
        print("\nResults:")
        print(f"{'Model':<40}{'Price':>10}{'1440p FPS':>15}{'Price per FPS':>20}{'URL':<100}")
        print("-" * 185)

        # Print each row of the table with Price per FPS rounded to 1 decimal
        for _, row in df.iterrows():
            print(f"{row['model']:<40}{row['price']:>10.2f}{row['1440p Ultra FPS']:>15.2f}{row['Price per FPS']:>20.1f}{row['canonical_url']:<100}")

def main():
    args = parse_args()

    # Get the input file, either from argument or by finding the latest
    input_file = args.file if args.file else find_latest_gpu_listings()

    try:
        # Load and process the data
        result_df = load_and_process_data(input_file, args.performance, args)

        # Display the results
        display_results(result_df, args.output_csv)

    except FileNotFoundError as e:
        print(f"Error: {e}")
        return 1
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return 1

    return 0

if __name__ == "__main__":
    exit(main())
