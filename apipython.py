import PyPDF2
<<<<<<< HEAD
import pandas as pd
import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables

=======
import requests
import os
import pandas as pd
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
>>>>>>> 9d2cc08 (increased summary)
api_key = os.getenv('HUGGINGFACE_API_KEY')

# Step 1: Extract Text from PDF
def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

<<<<<<< HEAD
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
=======
# Step 2: Truncate the text to fit within the model's token limit
def truncate_text(text, max_length=1024):
    return text[:max_length]  # Truncate the text to the first 1024 characters (adjust as needed)

# Step 3: Summarize using Hugging Face's API (with longer length settings)
def summarize_text_with_hf_api(text, api_key):
    headers = {"Authorization": f"Bearer {api_key}"}
    api_url = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
    
    # Set summarization parameters with a higher max_length to get a longer summary
    params = {
        "inputs": text,
        "parameters": {"max_length": 250, "min_length": 100, "do_sample": False}  # Increased length
    }
    
    try:
        response = requests.post(api_url, headers=headers, json=params)
        response.raise_for_status()  # Ensure we notice bad responses
        response_json = response.json()
        if isinstance(response_json, list) and 'summary_text' in response_json[0]:
            return response_json[0]['summary_text']
        else:
            return "No summary available"  # Default in case the response isn't structured as expected
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
        print("Response content:", response.content)
        return "Error in API call"
    except Exception as err:
        print(f"An error occurred: {err}")
        return "Error in API call"

# Step 4: Organize the summary into an Excel file
def organize_into_excel(summary, excel_file):
    df = pd.DataFrame([{"Summary": summary}])
    df.to_excel(excel_file, index=False)

# Example usage
pdf_file = "C:/Users/new mmc/Desktop/cv2.pdf"
text = extract_text_from_pdf(pdf_file)

# Truncate the text to fit the model's token limits
truncated_text = truncate_text(text)

# Summarize the truncated text into one paragraph with a longer summary
summary = summarize_text_with_hf_api(truncated_text, api_key)
print(f"Summary: {summary}")

# Save the summary into an Excel file
organize_into_excel(summary, "CV_Summary.xlsx")
>>>>>>> 9d2cc08 (increased summary)
