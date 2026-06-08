import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Get API key from .env
api_key = os.getenv("AIzaSyBOanSVJ8cYGhUV7BkMy-uL9ViZNbobI1A")

if not api_key:
    st.error("❌ Google API key not found! Please set GOOGLE_API_KEY in your .env file.")
else:
    genai.configure(api_key=api_key)

# Create Gemini model
model = genai.GenerativeModel("models/gemini-1.5-flash")



def chatbot_page():
    st.header("🤖 AI Tutor Chatbot")
    st.write("Ask your tutor anything related to your studies!")

    # Store messages in session state
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    # User input
    prompt = st.chat_input("Ask a question...")

    if prompt:
        # Append user's message
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Generate AI response
        with st.chat_message("assistant"):
            try:
                response = model.generate_content([prompt])  # FIX: Pass as list
                reply = response.text
            except Exception as e:
                reply = f"⚠️ Error: {str(e)}"

            # Append assistant's reply
            st.session_state.messages.append({"role": "assistant", "content": reply})
            st.write(reply)

# Run app
if __name__ == "__main__":
    chatbot_page()
