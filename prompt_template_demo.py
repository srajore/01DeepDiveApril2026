from langchain_core.prompts import PromptTemplate

from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

from langchain_ollama import ChatOllama

llm = ChatOllama(model="gpt-oss:120b-cloud")

#prompt = PromptTemplate.from_template(
#    "Help me with the key achievements of  {name} in 3 bullet points in 500 words."
#)

prompt = PromptTemplate(
    template="Help me with the key achievements of  {name} in 3 bullet points in 500 words.",
    input_variables=["name"]
)


chain = prompt | llm   #LCEL

name=input("please enter the name of the person you want to know about: ")

response= chain.invoke({"name": name })


print(response.content)