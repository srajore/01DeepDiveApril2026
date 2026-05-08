import sys
from typing import Any
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

def initialize_llm() -> ChatOllama:
    """Initializes and returns the ChatOllama model instance."""
    try:
        return ChatOllama(model="gpt-oss:120b-cloud")
    except Exception as e:
        print(f"Error: Failed to initialize LLM: {e}")
        sys.exit(1)

def create_prompt() -> ChatPromptTemplate:
    """Creates a generic ChatPromptTemplate for the assistant."""
    return ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant."),
        ("user", "{user_input}"),
    ])

def build_chain(prompt: ChatPromptTemplate, llm: ChatOllama) -> Any:
    """Builds the LCEL chain combining the prompt and the LLM."""
    return prompt | llm

def get_user_input() -> str:
    """Safely reads and sanitizes user input from the console."""
    try:
        return input("\nYou: ").strip()
    except (EOFError, KeyboardInterrupt):
        return "quit"

def generate_response(chain: Any, user_input: str) -> str:
    """Invokes the LCEL chain to generate a response for the given input."""
    try:
        response = chain.invoke({"user_input": user_input})
        return response.content if hasattr(response, 'content') else str(response)
    except Exception as e:
        return f"I'm sorry, I encountered an error: {e}"

def run_chatbot():
    """Orchestrates the chatbot loop."""
    print("--- Initializing Chatbot ---")
    llm = initialize_llm()
    prompt = create_prompt()
    chain = build_chain(prompt, llm)

    print("\nWelcome! I am your AI assistant. (Type 'exit' or 'quit' to stop)")

    try:
        while True:
            user_input = get_user_input()

            if not user_input:
                print("Assistant: Please enter a question or statement.")
                continue

            if user_input.lower() in ["exit", "quit"]:
                print("\nAssistant: Goodbye!")
                break

            response = generate_response(chain, user_input)
            print(f"Assistant: {response}")

    except KeyboardInterrupt:
        print("\n\nAssistant: Session interrupted. Goodbye!")
    except Exception as e:
        print(f"\nAssistant: A critical error occurred: {e}")

if __name__ == "__main__":
    run_chatbot()
