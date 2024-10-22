import pandas as pd
import argparse
import re

def parse_args():
    parser = argparse.ArgumentParser(
        description="Analyze GPU listings and find the best price-to-performance ratios.",
        epilog="This tool helps you find the best value GPUs based on price and 1440p performance."
    )
    parser.add_argument("-f", "--file", required=True, help="Path to the CSV file containing all GPU listings")
    parser.add_argument("-p", "--performance", required=True, help="Path to the CSV file containing 1440p performance data")
    parser.add_argument("-c", "--csv", help="Output results to a CSV file instead of console", dest="output_csv", metavar="OUTPUT_FILE")
    return parser.parse_args()

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

def standardize_gpu_name(name):
    # Remove 'GB' and any surrounding whitespace
    name = re.sub(r'\s*\d+\s*GB\s*', ' ', name)
    # Remove any duplicate whitespace
    name = re.sub(r'\s+', ' ', name).strip()
    return name

def load_and_process_data(listings_file, performance_file):
    # Get the cheapest price for each GPU model
    cheapest_df = parse_gpu_listings(listings_file)

    # Load the 1440p performance data
    performance_df = pd.read_csv(performance_file)

    # Standardize GPU names in both dataframes
    cheapest_df['standardized_model'] = cheapest_df['model'].apply(standardize_gpu_name)
    performance_df['standardized_model'] = performance_df['Graphics Card'].apply(standardize_gpu_name)

    # Merge the dataframes based on the standardized GPU model names
    merged_df = pd.merge(cheapest_df, performance_df, on='standardized_model', how='inner')

    # Calculate price per FPS
    merged_df['Price per FPS'] = merged_df['price'] / merged_df['1440p Ultra FPS']

    # Sort by Price per FPS
    sorted_df = merged_df.sort_values('Price per FPS')

    # Clean up the result
    result_df = sorted_df[['model', 'price', '1440p Ultra FPS', 'Price per FPS', 'canonical_url']]

    return result_df

def display_results(df, output_csv=None):
    if output_csv:
        # Output to CSV file
        df.to_csv(output_csv, index=False)
        print(f"Results have been saved to {output_csv}")
    else:
        # Print the table header
        print(f"{'Model':<40}{'Price':>10}{'1440p FPS':>15}{'Price per FPS':>20}{'URL':<100}")
        print("-" * 185)

        # Print each row of the table
        for _, row in df.iterrows():
            print(f"{row['model']:<40}{row['price']:>10.2f}{row['1440p Ultra FPS']:>15.2f}{row['Price per FPS']:>20.2f}{row['canonical_url']:<100}")

if __name__ == "__main__":
    args = parse_args()

    # Load and process the data
    result_df = load_and_process_data(args.file, args.performance)

    # Display the results
    display_results(result_df, args.output_csv)
