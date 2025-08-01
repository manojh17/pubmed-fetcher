import argparse
from pubmed_fetcher.core import fetch_and_process_results

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed papers with pharma/biotech affiliations.")
    parser.add_argument("query", help="PubMed query (quoted)")
    parser.add_argument("-f", "--file", help="Filename to save results as CSV")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug output")

    args = parser.parse_args()
    fetch_and_process_results(query=args.query, output_file=args.file, debug=args.debug)
