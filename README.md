PDF Summarizer using Hugging Face API
This project extracts text from a PDF, summarizes it using the Hugging Face API, and organizes the summarized text into an Excel file.

Features
Extract Text from PDF:
Uses PyPDF2 to extract text from a provided PDF file.
Summarization using Hugging Face's API:
Uses the Hugging Face facebook/bart-large-cnn model to summarize the extracted text via an API.
Organize Summaries into Excel:
Saves the summarized sections into an Excel file for easy viewing and distribution.
Requirements
Ensure you have Python 3.x installed and the following libraries:

PyPDF2
pandas
requests
python-dotenv
Install the required packages by running:

bash
Copy code
pip install PyPDF2 pandas requests python-dotenv
Environment Setup
Create a .env file in the root of your project.

Add your Hugging Face API key to the .env file like so:

bash
Copy code
HUGGINGFACE_API_KEY=your_hugging_face_api_key_here
Usage
Step 1: Extract Text from PDF
The script uses PyPDF2 to extract the entire text from a given PDF file.

Step 2: Summarize Text Using Hugging Face API
The extracted text is then divided into sections and summarized using the facebook/bart-large-cnn model from Hugging Face.

Step 3: Save Summaries in Excel
Each section of the text is summarized and stored in an Excel file using pandas.
