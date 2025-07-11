# 📧 Auto Email Response Generator (Streamlit Cloud Secure)

A secure, agentic AI app that generates smart, tone-based email replies using GPT-4. Fully deployable on **Streamlit Cloud** using their **Secrets Manager**.

---

## 🚀 Features
- Paste received email
- Choose tone: Professional, Friendly, Apologetic, Persuasive
- Get a natural GPT-4-powered reply
- Fully secure using Streamlit Cloud's Secrets Manager

---

## 🛠 Deployment Instructions (Streamlit Cloud)

### 1. Push to GitHub
- Create a repo and push these files
- Ensure `.streamlit/secrets.toml` is **NOT** added

### 2. Deploy on Streamlit Cloud
- Visit: [https://streamlit.io/cloud](https://streamlit.io/cloud)
- Create a new app from this GitHub repo
- Select `main.py` as the entry point

### 3. Add OpenAI API Key in Secrets
Go to your app’s Settings → Secrets and add:
```
OPENAI_API_KEY = "sk-xxxxxxxxxxxxxxxxxxxx"
```

### 4. Done 🎉
Your app is now live and secure.

---

## 📁 Project Structure
```
auto_email_agent_cloud/
├── main.py
├── agents/
│   └── email_agent.py
├── .streamlit/
│   └── config.toml
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🔐 Why Use Secrets Manager?
Using `st.secrets["OPENAI_API_KEY"]` keeps your API key:
- **Safe** (never exposed)
- **Deployable** (even from a public GitHub repo)
- **Editable** without touching the code

Happy coding!