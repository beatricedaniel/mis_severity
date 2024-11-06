# report_generation.py
import json
import pandas as pd

# Load settings
with open("settings.json", "r") as f:
    settings = json.load(f)

def generate_report(df: pd.DataFrame, output_path: str) -> None:
    """Generate a summary report of the classified observations."""
    summary = df.groupby(["topic", "severity"]).size().unstack(fill_value=0)
    summary.to_csv(output_path)
    print(f"Report generated at {output_path}")