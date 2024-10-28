import sys
from test_set import test_cases, mock_fetch_page, mock_fetch_description
from finngpu import match_gpu_model, load_gpu_models
from collections import defaultdict
import argparse

def validate_gpu_matching(verbose=False):
    """
    Validate GPU model matching against test cases
    """
    # Load GPU models
    gpu_models = load_gpu_models()

    # Track results
    results = {
        'total': len(test_cases),
        'correct': 0,
        'incorrect': 0,
        'mismatches': []
    }

    # Track error patterns
    error_patterns = defaultdict(int)

    print(f"\nValidating {len(test_cases)} test cases...\n")

    # Process each test case
    for ad_id, expected_model, title in test_cases:
        # First try matching just the title
        title_match, _, _, _, _, _ = match_gpu_model(title, gpu_models, debug=False)

        # If no match from title, try getting description and matching that
        description = None
        description_match = None
        if title_match == "Unknown":
            description = mock_fetch_description(f"https://www.finn.no/bap/forsale/ad.html?finnkode={ad_id}")
            if description:
                description_match, _, _, _, _, _ = match_gpu_model(description, gpu_models, debug=False)

        # Use title match if found, otherwise use description match if found
        matched_model = title_match if title_match != "Unknown" else (description_match if description_match else "Unknown")

        # Compare results
        if matched_model == expected_model:
            results['correct'] += 1
            if verbose:
                print(f"✓ Correct: {ad_id}")
                print(f"  Title: {title}")
                print(f"  Model: {matched_model}")
                if description:
                    print(f"  (Matched from description)")
                print()
        else:
            results['incorrect'] += 1
            error_patterns[f"{expected_model} → {matched_model}"] += 1

            if verbose:
                print(f"✗ Mismatch: {ad_id}")
                print(f"  Title: {title}")
                print(f"  Expected: {expected_model}")
                print(f"  Got: {matched_model}")
                if description:
                    print(f"  (Attempted description match)")
                print()

            results['mismatches'].append({
                'ad_id': ad_id,
                'title': title,
                'expected': expected_model,
                'got': matched_model,
                'used_description': bool(description and description_match)
            })

    # Calculate accuracy
    accuracy = results['correct'] / results['total'] * 100

    # Print results
    print("\nValidation Results:")
    print("-" * 50)
    print(f"Total test cases: {results['total']}")
    print(f"Correct matches: {results['correct']}")
    print(f"Incorrect matches: {results['incorrect']}")
    print(f"Accuracy: {accuracy:.1f}%")

    if results['incorrect'] > 0:
        print("\nError Patterns:")
        print("-" * 50)
        for pattern, count in sorted(error_patterns.items(), key=lambda x: x[1], reverse=True):
            print(f"{pattern}: {count}")

    return results

def main():
    parser = argparse.ArgumentParser(description="Validate FinnGPU model matching against test set")
    parser.add_argument("-v", "--verbose", action="store_true",
                       help="Show all matches, not just errors")
    args = parser.parse_args()

    try:
        results = validate_gpu_matching(verbose=args.verbose)

        # Exit with status code based on accuracy
        if results['incorrect'] == 0:
            print("\nAll tests passed! 🎉")
            return 0
        else:
            print("\nSome tests failed. See above for details.")
            return 1

    except Exception as e:
        print(f"Error during validation: {e}")
        return 2

if __name__ == "__main__":
    sys.exit(main())
