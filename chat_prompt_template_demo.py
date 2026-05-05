from langchain_core.prompts import ChatPromptTemplate

from langchain_ollama import ChatOllama

llm = ChatOllama(model="gpt-oss:120b-cloud")


prompt = ChatPromptTemplate([
    ("system", "You are a helpful assistant "),
    ("user", "Help me with the key achievements of  {name} in 3 bullet points ")
])
   


chain = prompt | llm   #LCEL

name=input("please enter the name of the person you want to know about: ")

response= chain.invoke({"name": name })


print(response.content)