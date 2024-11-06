# main.py
import argparse
import json
from src.text_extraction import extract_text
from src.preprocess import preprocess_pipeline
from src.classification import classify_observations
from src.report_generation import generate_report
import pandas as pd

# Load settings
with open("settings.json", "r") as f:
    settings = json.load(f)

def extract():
    """Extracts text from the hospital evaluation report."""
    text = extract_text(settings["data_file_path"], file_type=settings["file_type"])
    with open(settings["output_extracted_text_path"], "w") as f:
        f.write("\n".join(text))
    print(f"Text extraction complete. Output saved to {settings['output_extracted_text_path']}")

def preprocess():
    """Preprocesses the extracted text."""
    with open(settings["output_extracted_text_path"], "r") as f:
        text_pages = f.readlines()
    preprocessed_text = preprocess_pipeline(text_pages)
    with open(settings["output_preprocessed_text_path"], "w") as f:
        f.write("\n".join(preprocessed_text))
    print(f"Text preprocessing complete. Output saved to {settings['output_preprocessed_text_path']}")

def classify():
    """Classifies text into topics and evaluates severity levels."""
    with open(settings["output_preprocessed_text_path"], "r") as f:
        preprocessed_text = f.readlines()
    df = classify_observations(preprocessed_text, settings["topics"])
    df.to_csv(settings["output_classified_report_path"], index=False)
    print(f"Classification complete. Output saved to {settings['output_classified_report_path']}")

def report():
    """Generates a summary report based on classification results."""
    df = pd.read_csv(settings["output_classified_report_path"])
    generate_report(df, settings["output_summary_report_path"])
    print(f"Report generation complete. Summary saved to {settings['output_summary_report_path']}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process hospital evaluation report.")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Extract command
    subparsers.add_parser("extract", help="Extract text from the document")

    # Preprocess command
    subparsers.add_parser("preprocess", help="Preprocess the extracted text")

    # Classify command
    subparsers.add_parser("classify", help="Classify text into topics and assess severity")

    # Report command
    subparsers.add_parser("report", help="Generate summary report of classifications")

    args = parser.parse_args()

    # Execute the command based on user input
    if args.command == "extract":
        extract()
    elif args.command == "preprocess":
        preprocess()
    elif args.command == "classify":
        classify()
    elif args.command == "report":
        report()
    else:
        parser.print_help()