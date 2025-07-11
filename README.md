# 📧 Auto Email Response Generator (Secure)

A Streamlit app powered by GPT-4 that generates professional, friendly, or persuasive email replies automatically.

## ✅ Secure Setup
- API key is stored in `.streamlit/secrets.toml` (NEVER push it to public GitHub).
- Use `st.secrets["OPENAI_API_KEY"]` to access it.

## 🛠 Local Setup
1. Clone repo and create `.streamlit/secrets.toml` with your key:
   ```
   OPENAI_API_KEY = "sk-xxxxxxx..."
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the app:
   ```
   streamlit run main.py
   ```

## ☁️ Streamlit Cloud Deployment
- Add your secret in the **Secrets Manager** under app settings:
  ```
  OPENAI_API_KEY = sk-xxxxxxx...
  ```