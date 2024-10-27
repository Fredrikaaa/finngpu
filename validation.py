# validation.py

import pandas as pd
from typing import Dict, List, Tuple, Optional
from datetime import datetime

def validate_gpu_matching(
    listings_df: pd.DataFrame, 
    test_cases: List[Tuple[str, str, str]], 
    verbose: bool = False,
    save_results: bool = True
) -> Dict:
    """
    Validate GPU matching results against test cases
    
    Args:
        listings_df: DataFrame with GPU listings, must contain 'ad_id' and 'model' columns
        test_cases: List of (ad_id, expected_model, title) tuples
        verbose: Whether to print detailed results
        save_results: Whether to save results to CSV
        
    Returns:
        Dict containing validation metrics:
        {
            'total': total number of test cases,
            'correct': number of correct matches,
            'not_found': number of listings not found,
            'accuracy': overall accuracy,
            'accuracy_excluding_not_found': accuracy excluding not found cases,
            'mismatches': list of (expected, actual, title) for incorrect matches
        }
    """
    if test_cases is None:
        raise ValueError("No test cases provided")
        
    if not {'ad_id', 'model'}.issubset(listings_df.columns):
        raise ValueError("DataFrame must contain 'ad_id' and 'model' columns")
        
    results = []
    for ad_id, expected_model, title in test_cases:
        # Find the matching row in the DataFrame
        matched_row = listings_df[listings_df['ad_id'] == ad_id]
        
        if matched_row.empty:
            if verbose:
                print(f"\nAd {ad_id} not found in dataset")
                print(f"Expected: {expected_model}")
                print(f"Title: {title}")
            results.append((ad_id, expected_model, "Not Found", title))
            continue
            
        actual_model = matched_row['model'].iloc[0]
        
        if verbose or actual_model != expected_model:
            print(f"\nAd {ad_id}:")
            print(f"Title: {title}")
            print(f"Expected: {expected_model}")
            print(f"Got: {actual_model}")
            if actual_model != expected_model:
                print("MISMATCH ❌")
            else:
                print("Match ✓")
            
        results.append((ad_id, expected_model, actual_model, title))
    
    # Calculate statistics
    total = len(test_cases)
    correct = sum(1 for _, expected, actual, _ in results if expected == actual)
    not_found = sum(1 for _, _, actual, _ in results if actual == "Not Found")
    accuracy = correct / total if total > 0 else 0
    
    # Calculate accuracy excluding not found cases
    found_cases = total - not_found
    accuracy_excluding_not_found = (
        sum(1 for _, expected, actual, _ in results 
            if actual != "Not Found" and expected == actual) / found_cases
        if found_cases > 0 else 0
    )
    
    # Collect mismatches
    mismatches = [(expected, actual, title) for _, expected, actual, title in results 
                  if actual != "Not Found" and expected != actual]
    
    # Print results if verbose
    if verbose:
        print(f"\nValidation Results:")
        print(f"Total test cases: {total}")
        print(f"Correct matches: {correct}")
        print(f"Accuracy: {accuracy:.2%}")
        print(f"Not found in dataset: {not_found}")
        print(f"Accuracy (excluding not found): {accuracy_excluding_not_found:.2%}")
        
        if mismatches:
            print("\nMismatch Analysis:")
            mismatch_types = {}
            for expected, actual, _ in mismatches:
                key = f"{expected} → {actual}"
                mismatch_types[key] = mismatch_types.get(key, 0) + 1
                
            for mtype, count in sorted(mismatch_types.items(), key=lambda x: x[1], reverse=True):
                print(f"{mtype}: {count}")
    
    # Save results if requested
    if save_results:
        results_df = pd.DataFrame(results, 
                                columns=['ad_id', 'expected_model', 'actual_model', 'title'])
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        results_file = f"validation_results_{timestamp}.csv"
        results_df.to_csv(results_file, index=False)
        if verbose:
            print(f"\nDetailed results saved to {results_file}")
    
    # Return validation metrics
    return {
        'total': total,
        'correct': correct,
        'not_found': not_found,
        'accuracy': accuracy,
        'accuracy_excluding_not_found': accuracy_excluding_not_found,
        'mismatches': mismatches
    }

def main():
    """
    Command-line interface for validation
    """
    import argparse
    
    parser = argparse.ArgumentParser(description="Validate GPU matching results")
    parser.add_argument("listings", help="Path to CSV file with GPU listings")
    parser.add_argument("--verbose", "-v", action="store_true", 
                       help="Print detailed results")
    parser.add_argument("--no-save", action="store_true",
                       help="Don't save results to CSV")
    args = parser.parse_args()
    
    try:
        # Load listings
        listings_df = pd.read_csv(args.listings)
        
        # Import test cases
        from test_set import test_cases
        
        # Run validation
        validate_gpu_matching(
            listings_df, 
            test_cases, 
            verbose=args.verbose,
            save_results=not args.no_save
        )
        
    except Exception as e:
        print(f"Error: {e}")
        return 1
        
    return 0

if __name__ == "__main__":
    exit(main())
