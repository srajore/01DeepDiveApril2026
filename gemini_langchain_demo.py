from langchain_google_genai import ChatGoogleGenerativeAI


from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

llm = ChatGoogleGenerativeAI(model="gemini-3-flash-preview")

response = llm.invoke("What is the capital of India?")

print(response.content)
