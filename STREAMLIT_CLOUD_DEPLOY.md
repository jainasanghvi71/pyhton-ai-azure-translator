# Deploying to Streamlit Community Cloud

Follow these steps to deploy your Streamlit app to Streamlit Community Cloud:

## 1. Prepare Your Repository

- Ensure your code is pushed to a public GitHub repository.
- Your main app file should be named `main.py` (or update the path in Streamlit Cloud settings).
- Include a `requirements.txt` file listing all dependencies (e.g., streamlit, requests, python-dotenv, azure-ai-translation-text).
- Do **not** commit your `.env` file. You will add secrets in the Streamlit Cloud UI.

## 2. Create `requirements.txt`

If you don't have one, create a `requirements.txt` with:

```
streamlit
requests
python-dotenv
azure-ai-translation-text
```

## 3. Push to GitHub

- Commit and push all your code to GitHub.

## 4. Deploy on Streamlit Community Cloud

- Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
- Sign in with your GitHub account.
- Click **New app**.
- Select your repository, branch, and set the main file path (e.g., `main.py`).

## 5. Set Environment Variables

- In the app settings, add your Azure secrets as environment variables:
  - `AZURE_TRANSLATOR_KEY`
  - `AZURE_TRANSLATOR_ENDPOINT`
  - `AZURE_TRANSLATOR_REGION`
- Use the same values as in your local `.env` file.

## 6. Deploy

- Click **Deploy**.
- Wait for the build to finish. Your app will be live at a public URL.

## 7. Update

- Any time you push changes to GitHub, your app will automatically redeploy.

---

For more help, see the [Streamlit Cloud documentation](https://docs.streamlit.io/streamlit-community-cloud).
