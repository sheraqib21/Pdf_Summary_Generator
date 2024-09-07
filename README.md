# PDF Text Extraction and Summarization

This project extracts text from a PDF file, summarizes it using Hugging Face's API, and organizes the summaries into an Excel file.

## Features

- Extracts text from a PDF file using `PyPDF2`
- Summarizes text using Hugging Face's `facebook/bart-large-cnn` model
- Organizes the summarized text into an Excel file using `pandas`

## Requirements

Before running the project, ensure you have the following libraries installed:

- `PyPDF2`
- `pandas`
- `requests`
- `python-dotenv`

You can install these packages using the following command:

```bash
pip install PyPDF2 pandas requests python-dotenv
```

# Installation 

```bash
git clone https://github.com/yourusername/yourproject.git
cd yourproject
```

Create a .env file in the root directory and add your Hugging Face API key.

```bash
HUGGINGFACE_API_KEY=your_huggingface_api_key
```
