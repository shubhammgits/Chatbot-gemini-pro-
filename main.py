import os
import time

import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
from google.api_core import exceptions


load_dotenv(override=True)

st.set_page_config(
    page_title="Chat with Gemini",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="auto"
)


def _get_secret(key: str):
    try:
        return st.secrets.get(key)
    except FileNotFoundError:
        # Local runs often don't have a secrets.toml file.
        return None


GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY") or _get_secret("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    st.error(
        "Missing `GOOGLE_API_KEY`.\n\n"
        "- Local: create a `.env` file with `GOOGLE_API_KEY=...`\n"
        "- Streamlit Cloud: set it in **App secrets** as `GOOGLE_API_KEY`"
    )
    st.stop()

genai.configure(api_key=GOOGLE_API_KEY)

MODEL_NAME = os.getenv("GEMINI_MODEL") or _get_secret("GEMINI_MODEL") or "gemini-1.5-flash"
MODEL_NAME = MODEL_NAME.removeprefix("models/")
model = genai.GenerativeModel(MODEL_NAME)


def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role


# If the model changes (e.g. you edit GEMINI_MODEL), reset the chat session.
if st.session_state.get("chat_model_name") != MODEL_NAME:
    st.session_state.chat_model_name = MODEL_NAME
    st.session_state.chat_session = model.start_chat(history=[])
elif "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

st.title("🤖 Chat with Gemini")

for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)

user_prompt = st.chat_input("Type your message here...")
if user_prompt:
    st.chat_message("user").markdown(user_prompt)

    gemini_response = None
    try:
        gemini_response = st.session_state.chat_session.send_message(user_prompt)
    except exceptions.GoogleAPICallError as e:
        st.error(f"Gemini API request failed ({type(e).__name__}).")
        st.info(
            "Common causes: invalid model name, missing/invalid API key, or your key doesn't have access to the model."
        )
        st.info("If you're on Streamlit Cloud: open **Manage app → Logs** for full details.")

    if gemini_response is not None:
        with st.chat_message("assistant"):
            st.markdown(gemini_response.text)