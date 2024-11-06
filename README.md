# Hospital Evaluation Report Processing

This project automates the extraction, preprocessing, classification, and reporting of observations from hospital evaluation documents. It takes a `.docx` file containing paragraphs and tables, processes it to identify occurrences of treatment issues, categorizes them by topics, and evaluates severity levels. The final output includes a classified report and a summary report.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Output Files](#output-files)
- [Troubleshooting](#troubleshooting)

---

## Overview

The project automates a multi-step pipeline:
1. **Text Extraction**: Extracts text from both paragraphs and tables in `.docx` documents.
2. **Preprocessing**: Cleans and lemmatizes the text for easier analysis.
3. **Classification**: Classifies observations based on predefined topics and assigns severity levels.
4. **Reporting**: Generates a detailed report and a summary report, both saved as CSV files.

---

## Features

- **Multi-source Text Extraction**: Supports extraction from both paragraphs and tables in `.docx` files.
- **Natural Language Processing (NLP)**: Uses NLP for cleaning and lemmatization, ensuring high-quality text data.
- **Classification & Severity Analysis**: Classifies issues by topic and severity, providing valuable insights.
- **Modular Design**: Each step is modular, making the project flexible and easy to customize.
- **Easy Command Line Interface**: Run individual steps or the full pipeline from the command line.

---

## Project Structure

The project is organized as follows:

```plaintext
hospital-evaluation-report/
│
├── main.py               # Main script to run each stage of the pipeline
├── settings.json         # Configuration file with paths, topics, etc.
├── requirements.txt      # List of required Python libraries
├── README.md             # Project documentation
│
├── src/                  # Directory containing the main processing scripts
│   ├── text_extraction.py       # Extracts text from .docx files
│   ├── preprocess.py            # Preprocesses and cleans the extracted text
│   ├── classification.py        # Classifies text into topics and severity
│   └── report_generation.py     # Generates final summary report
│
└── output/               # Directory where output files are saved
```

## Installation

1. Clone the Repository
```bash
git clone https://github.com/beatricedaniel/mis_severity.git
cd mis_severity
```

2. Install Dependencies
Make sure you have Python 3.7+ installed. Then, install the required packages:
```bash
pip install -r requirements.txt
```

3. Download spaCy Language Model
This project uses the small French language model in spaCy. Install it by running:
```bash
python -m spacy download fr_core_news_sm
```

## Usage

The project is managed through ```main.py```, which accepts specific commands to run each part of the pipeline. Here are the available commands:

1. Extract Text
To extract text from the document (both paragraphs and tables):
```bash
python main.py extract
```
This will save the raw extracted text to ```output/extracted_text.txt```.

2. Preprocess Text

To preprocess and clean the extracted text:
```bash
python main.py preprocess
```
This will save the preprocessed text to ```output/preprocessed_text.txt```.

3. Classify Observations

To classify the observations into topics and assign severity levels:
```bash
python main.py classify
```
This will save the classified observations to ```output/classified_report.csv```.

4. Generate Summary Report

To generate a summary report of the classifications:
```bash
python main.py report
```
This will save the summary to ```output/summary_report.csv```.

## Configuration

All configuration settings are managed through the settings.json file. Key parameters include:

* ```data_file_path```: Path to the input .docx file.
* ```output_extracted_text_path```: Path to save extracted text.
* ```output_preprocessed_text_path```: Path to save preprocessed text.
* ```output_classified_report_path```: Path to save the classified report.
* ```output_summary_report_path```: Path to save the summary report.
* ```topics```: A list of topics for classification (e.g., "patient safety", "medication errors").
* ```file_type```: Specify the file type ("docx" for this project).

## Output Files

* **Extracted Text** (```output/extracted_text.txt```): Raw text extracted from the .docx file, including paragraphs and tables.
* **Preprocessed Text** (```output/preprocessed_text.txt```): Cleaned and lemmatized text, ready for classification.
* **Classified Report** (```output/classified_report.csv```): Detailed classification of observations by topic and severity.
* **Summary Report** (```output/summary_report.csv```): Aggregated report of topic and severity counts, suitable for analysis.

## Troubleshooting

Common Issues
1. Error: Unsupported file type
Ensure that ```file_type``` in ```settings.json``` is set to "docx".
2. Missing en_core_web_sm Model
Run ```python -m spacy download en_core_web_sm``` to install the spaCy model.
3. File Paths
Verify that paths in ```settings.json``` are correct. If directories do not exist, create them manually.