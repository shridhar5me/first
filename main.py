import streamlit as st
from email_agent import generate_email_response

st.set_page_config(page_title="Auto Email Responder", layout="wide")
st.title("📧 Auto Email Response Generator")

email_text = st.text_area("Paste the email content you received:", height=300)

tone = st.selectbox("Select response tone", ["Professional", "Friendly", "Apologetic", "Persuasive"])

if st.button("Generate Response"):
    with st.spinner("Crafting your perfect reply..."):
        response = generate_email_response(email_text, tone)
        st.subheader("✉️ Suggested Response")
        st.markdown(response, unsafe_allow_html=True)