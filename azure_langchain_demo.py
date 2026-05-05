from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

llm = AzureChatOpenAI(
    azure_deployment="gpt-4o-mini",  # or your deployment
    api_version="2024-12-01-preview",  # or your api version
)


response = llm.invoke("Who am I? could you explain it in spritual way")

print(response.content)