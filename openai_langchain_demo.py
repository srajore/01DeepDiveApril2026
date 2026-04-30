from langchain_openai import ChatOpenAI


from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

llm = ChatOpenAI(model="gpt-4.1-mini")

response = llm.invoke("What is the capital of India?")

print(response.content)