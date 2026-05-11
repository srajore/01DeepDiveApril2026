import sys
from typing import Any
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama


# -------------------------------
# LLM Initialization
# -------------------------------
def initialize_llm() -> ChatOllama:
    try:
        return ChatOllama(model="gpt-oss:120b-cloud")
    except Exception as e:
        print(f"Error: Failed to initialize LLM: {e}")
        sys.exit(1)


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
def build_chain(prompt: ChatPromptTemplate, llm: ChatOllama) -> Any:
    return prompt | llm


# -------------------------------
# Input Handler
# -------------------------------
def get_user_input() -> str:
    try:
        return input("\nYou: ").strip()
    except (EOFError, KeyboardInterrupt):
        return "quit"


# -------------------------------
# Main Chat Loop
# -------------------------------
def run_chatbot():
    print("--- Initializing Chatbot ---")

    llm = initialize_llm()
    prompt = create_prompt()
    chain = build_chain(prompt, llm)

    print("\nWelcome! I am your AI assistant. (Type 'exit' or 'quit' to stop)")

    # ✅ Simple in-memory conversation history
    messages = []

    try:
        while True:
            user_input = get_user_input()

            if not user_input:
                print("Assistant: Please enter a question or statement.")
                continue

            if user_input.lower() in ["exit", "quit"]:
                print("\nAssistant: Goodbye!")
                break

            # ✅ Add user message
            messages.append(("user", user_input))
            #print(messages)

            # ✅ Generate response
            response = chain.invoke({"messages": messages})
            response_text = response.content  # simplified

            # ✅ Store assistant response
            messages.append(("assistant", response_text))
            #print(messages)
            print(f"Assistant: {response_text}")

    except KeyboardInterrupt:
        print("\n\nAssistant: Session interrupted. Goodbye!")
    except Exception as e:
        print(f"\nAssistant: A critical error occurred: {e}")


# -------------------------------
# Entry Point
# -------------------------------
if __name__ == "__main__":
    run_chatbot()