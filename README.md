# AI Chatbot Project

A modular, testable, CLI-based chatbot implementation using LangChain (LCEL) and ChatOllama.

## 🚀 Features
- **Modular Architecture**: Clear separation between LLM initialization, prompt creation, and chain building.
- **LCEL Integration**: Uses LangChain Expression Language (`prompt | llm`) for a clean, declarative pipeline.
- **Robust Error Handling**: Handles LLM initialization failures and user input interruptions (EOF, KeyboardInterrupt) gracefully.
- **Stateless Design**: A simple, a-memory chatbot focused on single-turn interactions.

## 🛠️ Tech Stack
- **Language**: Python
- **Framework**: LangChain (Core)
- **LLM**: ChatOllama (`gpt-oss:120b-cloud`)
- **Environment**: `python-dotenv` for dotenv management

## 📂 Project Structure
- `chatbot.py`: The core chatbot implementation.
- `chatbot_spec.md`: Detailed functional and technical specifications.
- `test_chatbot.py`: Pytest suite to ensure specification compliance.
- `requirements.txt`: Project dependencies.
- `various_demo_files`: A collection of demonstration scripts for different LLM providers (Azure, OpenAI, Claude, Gemini, Groq, Ollama).

## 🚦 Getting Started

### 1. Installation
```bash
# Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configuration
Create a `.env` file in the root directory with necessary environment variables (if applicable).

### 3. Running the Chatbot
```bash
python chatbot.py
```

### 4. Running Tests
```bash
pytest test_chatbot.py
```

## 📜 Specification Compliance
The chatbot is built to strictly adhere to the `chatbot_spec.md` document, ensuring:
- No use of memory, agents, or tools.
- yang a-memory chatbot focused on single-turn interactions.
- Mandatory type hints and docstrings.
- Specific CLI interaction contracts.
- Exit codes for critical failures (`SystemExit(1)`).
