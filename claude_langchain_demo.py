from langchain_anthropic import ChatAnthropic

from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

llm= ChatAnthropic(model_name="claude-haiku-4-5-20251001")

response = llm.invoke("What is the capital of USA?")

print(response.content)

