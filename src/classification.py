# classification.py
import json
import pandas as pd
from transformers import pipeline

# Load settings
with open("settings.json", "r") as f:
    settings = json.load(f)

# Load a pre-trained BERT model for text classification
classifier = pipeline("zero-shot-classification")

def classify_text(text: str, topics: List[str]) -> dict:
    """Classify text into predefined topics using zero-shot classification."""
    result = classifier(text, candidate_labels=topics)
    return {"text": text, "topic": result["labels"][0], "score": result["scores"][0]}

def classify_severity(text: str) -> str:
    """Classify severity level based on keywords."""
    if any(keyword in text for keyword in ["severe", "critical", "life-threatening"]):
        return "severe"
    elif any(keyword in text for keyword in ["moderate", "concerning"]):
        return "moderate"
    else:
        return "mild"

def classify_observations(text_data: List[str], topics: List[str]) -> pd.DataFrame:
    """Classify observations by topic and severity."""
    classified_data = [classify_text(text, topics) for text in text_data]
    df = pd.DataFrame(classified_data)
    df["severity"] = df["text"].apply(classify_severity)
    return df
