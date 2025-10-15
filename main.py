
import streamlit as st
from dotenv import load_dotenv
import os
import requests

load_dotenv()
# Load environment variables
AZURE_TRANSLATOR_KEY = os.getenv("AZURE_TRANSLATOR_KEY")
AZURE_TRANSLATOR_ENDPOINT = os.getenv("AZURE_TRANSLATOR_ENDPOINT")
AZURE_TRANSLATOR_REGION = os.getenv("AZURE_TRANSLATOR_REGION")

# Ensure endpoint ends with /translator/text/v3.0 only if not already present
if AZURE_TRANSLATOR_ENDPOINT:
	if not AZURE_TRANSLATOR_ENDPOINT.rstrip('/').endswith('translator/text/v3.0'):
		AZURE_TRANSLATOR_ENDPOINT = AZURE_TRANSLATOR_ENDPOINT.rstrip('/') + '/translator/text/v3.0'

# Function to translate text using Azure Translator

def translate_text(text, to_language):
	path = '/translate?api-version=3.0'
	params = f'&to={to_language}'
	constructed_url = AZURE_TRANSLATOR_ENDPOINT.rstrip('/') + path + params
	headers = {
		'Ocp-Apim-Subscription-Key': AZURE_TRANSLATOR_KEY,
		'Ocp-Apim-Subscription-Region': AZURE_TRANSLATOR_REGION,
		'Content-type': 'application/json',
	}
	body = [{ 'text': text }]
	response = requests.post(constructed_url, headers=headers, json=body)
	if response.status_code == 200:
		result = response.json()
		return result[0]['translations'][0]['text']
	else:
		return f"Error: {response.status_code} - {response.text}"


st.set_page_config(page_title="Azure AI Translator", page_icon="🌐", layout="centered")
st.title("🌐 Azure AI Translator")
st.write("Enter your text below and select a target language code (e.g., 'fr' for French, 'es' for Spanish, 'hi' for Hindi). Powered by Azure AI.")

input_text = st.text_area("Text to translate", "Hello, world!")
target_lang = st.text_input("Target language code (e.g. fr, es)")

if st.button("Translate"):
	if input_text.strip():
		translated = translate_text(input_text, target_lang)
		st.success(f"Translated Text: {translated}")
	else:
		st.warning("Please enter text to translate.")