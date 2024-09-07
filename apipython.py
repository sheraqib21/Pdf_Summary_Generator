import PyPDF2
import pandas as pd
import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables

api_key = os.getenv('HUGGINGFACE_API_KEY')

# Step 1: Extract Text from PDF
def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# Step 2: Summarize using Hugging Face's API
def summarize_text_with_hf_api(text, api_key):
    headers = {"Authorization": f"Bearer {api_key}"}
    api_url = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
    try:
        response = requests.post(api_url, headers=headers, json={"inputs": text})
        response.raise_for_status()  # Ensure we notice bad responses
        response_json = response.json()
        print("Response JSON:", response_json)  # Print the full response for debugging
        summary = response_json[0].get('summary_text', 'No summary_text found in response')
        return summary
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
        print("Response content:", response.content)
    except Exception as err:
        print(f"An error occurred: {err}")

# Step 3: Organize the summaries into an Excel file
def organize_into_excel(summary_dict, excel_file):
    df = pd.DataFrame(list(summary_dict.items()), columns=['Section', 'Summary'])
    df.to_excel(excel_file, index=False)

# Example usage
pdf_file = "/Users/vyro/Desktop/cvpdf.pdf"
text = extract_text_from_pdf(pdf_file)

# Assuming you manually divide text into sections or automate this
sections = text.split("\n\n")  # This splits based on paragraph breaks, adjust as needed
summary_dict = {}
for i, section in enumerate(sections):
    summary = summarize_text_with_hf_api(section, api_key)
    summary_dict[f'Section {i+1}'] = summary

organize_into_excel(summary_dict, "CV_Summary.xlsx")
