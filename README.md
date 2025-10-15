# 🌐 Python AI Azure Translator

A simple Python project that integrates **Azure AI Translator Service** to perform real-time multilingual text translation using Azure AI Foundry.

This repo demonstrates how to:

- 🔑 Authenticate using Azure Translator key and endpoint
- 🌍 Detect and translate text between multiple languages
- 📘 Run translations directly from Python scripts
- ⚙️ Load API credentials securely using environment variables

## 🚀 Features

✅ Language detection and automatic translation  
✅ Supports multiple languages (en, de, es, fr, zh, etc.)  
✅ REST API and SDK-based examples  
✅ `.env`-based configuration for secure key management  
✅ Ready-to-run Python Script exmaple

🧰 Tech Stack

🐍 Python 3.x
☁️ Azure AI Foundry - AI translator
⚙️ requests, python-dotenv, uuid, json

## 🧩 Prerequisites

- Python 3.8 or higher
- Azure Translator resource in Azure Portal
  - Get your **Endpoint** and **Key** from  
    👉 [https://portal.azure.com](https://portal.azure.com)

## ⚙️ Setup Instructions

```bash
1. git clone https://github.com/jainasanghvi71/pyhton-ai-azure-translator.git
cd python-ai-azure-translator
```

2. **Setup virtual environement**
   python -m venv venv
   venv\Scripts\activate # Windows

3. **_Install dependencies_**
   pip install -r requirements.txt

4. Add your Azure credentials

Create a .env file in the project root:
AZURE_TRANSLATOR_KEY=your_azure_translator_key_here
AZURE_TRANSLATOR_ENDPOINT=https://api.cognitive.microsofttranslator.com/

5. **Run Stremalit**
   streamlit run main.py
