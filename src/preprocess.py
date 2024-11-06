# preprocess.py
import re
import json
from typing import List
import spacy

# Load settings
with open("settings.json", "r") as f:
    settings = json.load(f)

# Load the French language model
nlp = spacy.load(config['language_model'])

def clean_text(text: str) -> str:
    """Remove unwanted characters and normalize text."""
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)  # Remove special characters
    return text.lower()

def preprocess_text(text_pages: List[str]) -> List[str]:
    """Preprocesses a list of text pages, cleaning and tokenizing."""
    return [clean_text(page) for page in text_pages]

def lemmatize_text(text: str) -> str:
    """Lemmatizes the input text."""
    doc = nlp(text)
    return " ".join([token.lemma_ for token in doc if not token.is_stop])

def preprocess_pipeline(text_pages: List[str]) -> List[str]:
    """Apply preprocessing and lemmatization to all pages."""
    cleaned_text = preprocess_text(text_pages)
    return [lemmatize_text(page) for page in cleaned_text]
