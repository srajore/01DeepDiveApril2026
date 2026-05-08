import pytest
from unittest.mock import MagicMock, patch
from chatbot import (
    initialize_llm,
    create_prompt,
    build_chain,
    get_user_input,
    generate_response,
    run_chatbot
)
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

# --- Tests for initialize_llm ---

def test_initialize_llm_success():
    """Test successful initialization of the LLM."""
    llm = initialize_llm()
    assert isinstance(llm, ChatOllama)
    assert llm.model == "gpt-oss:120b-cloud"

def test_initialize_llm_failure():
    """Test LLM initialization failure handling (should exit)."""
    with patch("chatbot.ChatOllama", side_effect=Exception("Connection Error")):
        with pytest.raises(SystemExit) as e:
            initialize_llm()
        assert e.value.code == 1

# --- Tests for create_prompt ---

def test_create_prompt():
    """Test that the prompt is created as a ChatPromptTemplate with correct structure."""
    prompt = create_prompt()
    assert isinstance(prompt, ChatPromptTemplate)
    # Check if the prompt contains our expected system message
    messages = prompt.messages
    assert any("You are a helpful assistant." in str(m) for m in messages)

# --- Tests for build_chain ---

def test_build_chain():
    """Test that the build_chain returns a runnable chain."""
    prompt = create_prompt()
    llm = MagicMock(spec=ChatOllama)
    chain = build_chain(prompt, llm)
    # In LCEL, prompt | llm returns a Runnable sequence
    assert chain is not None

# --- Tests for get_user_input ---

def test_get_user_input_success():
    """Test standard user input."""
    with patch("builtins.input", return_value="  Hello AI!  "):
        result = get_user_input()
        assert result == "Hello AI!"  # Should be stripped

def test_get_user_input_empty():
    """Test empty user input."""
    with patch("builtins.input", return_value="   "):
        result = get_user_input()
        assert result == ""

def test_get_user_input_interrupt():
    """Test KeyboardInterrupt handling."""
    with patch("builtins.input", side_effect=KeyboardInterrupt):
        result = get_user_input()
        assert result == "quit"

def test_get_user_input_eof():
    """Test EOFError handling."""
    with patch("builtins.input", side_effect=EOFError):
        result = get_user_input()
        assert result == "quit"

# --- Tests for generate_response ---

def test_generate_response_success():
    """Test successful chain invocation."""
    mock_chain = MagicMock()
    mock_response = MagicMock()
    mock_response.content = "This is a test response"
    mock_chain.invoke.return_value = mock_response

    result = generate_response(mock_chain, "Hello")
    assert result == "This is a test response"

def test_generate_response_string_output():
    """Test when the chain returns a string instead of a Message object."""
    mock_chain = MagicMock()
    mock_chain.invoke.return_value = "String response"

    result = generate_response(mock_chain, "Hello")
    assert result == "String response"

def test_generate_response_error():
    """Test error handling during chain invocation (Negative Case)."""
    mock_chain = MagicMock()
    mock_chain.invoke.side_effect = Exception("LLM Timeout")

    result = generate_response(mock_chain, "Hello")
    assert "I'm sorry, I encountered an error" in result
    assert "LLM Timeout" in result

# --- Tests for run_chatbot loop (Integration) ---

def test_run_chatbot_exit_immediate():
    """Test that the chatbot exits immediately when 'exit' is provided."""
    with patch("chatbot.initialize_llm", return_value=MagicMock()), \
         patch("chatbot.get_user_input", return_value="exit"), \
         patch("builtins.print") as mock_print:

        run_chatbot()
        # Verify that the goodbye message was printed
        mock_print.assert_any_call("\nAssistant: Goodbye!")

def test_run_chatbot_flow():
    """Test a full cycle: valid input -> response -> exit."""
    mock_chain = MagicMock()
    mock_res = MagicMock()
    mock_res.content = "Hello there!"
    mock_chain.invoke.return_value = mock_res

    # Use a list of inputs to simulate the sequence of user actions
    # 1. Valid input, 2. Empty input (should prompt again), 3. Exit
    inputs = ["Hello", "", "quit"]

    with patch("chatbot.initialize_llm", return_value=MagicMock()), \
         patch("chatbot.build_chain", return_value=mock_chain), \
         patch("chatbot.get_user_input", side_effect=inputs), \
         patch("builtins.print") as mock_print:

        run_chatbot()

        # Verify response was printed
        mock_print.assert_any_call("Assistant: Hello there!")
        # Verify empty input warning was printed
        mock_print.assert_any_call("Assistant: Please enter a question or statement.")
        # Verify exit message
        mock_print.assert_any_call("\nAssistant: Goodbye!")
