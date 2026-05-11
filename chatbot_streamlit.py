import sys
from typing import Any
from dotenv import load_dotenv

import streamlit as st

load_dotenv()

from langchain_core.prompts import ChatPromptTemplate
#from langchain_ollama import ChatOllama
from langchain_google_genai import ChatGoogleGenerativeAI


# -------------------------------
# LLM Initialization
# -------------------------------
@st.cache_resource
def initialize_llm() -> ChatGoogleGenerativeAI:
    try:
        return ChatGoogleGenerativeAI(model="gemini-3-flash-preview")
    except Exception as e:
        st.error(f"Failed to initialize LLM: {e}")
        st.stop()


# -------------------------------
# Prompt (Memory-enabled)
# -------------------------------
def create_prompt() -> ChatPromptTemplate:
    return ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant."),
        ("placeholder", "{messages}")
    ])


# -------------------------------
# Chain Builder
# -------------------------------
def build_chain(prompt: ChatPromptTemplate, llm: ChatGoogleGenerativeAI) -> Any:
    return prompt | llm


# -------------------------------
# App UI
# -------------------------------
def run_streamlit_app():
    st.set_page_config(page_title="Chatbot", layout="centered")

    st.title("💬 AI Chatbot")

    llm = initialize_llm()
    prompt = create_prompt()
    chain = build_chain(prompt, llm)

    # ✅ Session-based memory (equivalent to messages = [])
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for role, content in st.session_state.messages:
        with st.chat_message(role):
            st.markdown(content)

    # Input box
    user_input = st.chat_input("Type your message...")

    if user_input:
        # Add user message
        st.session_state.messages.append(("user", user_input))

        with st.chat_message("user"):
            st.markdown(user_input)

        # Generate response
        try:
            response = chain.invoke({"messages": st.session_state.messages})
            response_text = response.content
        except Exception as e:
            response_text = f"Error: {e}"

        # Add assistant response
        st.session_state.messages.append(("assistant", response_text))

        with st.chat_message("assistant"):
            st.markdown(response_text)


# -------------------------------
# Entry Point
# -------------------------------
if __name__ == "__main__":
    run_streamlit_app()