from langchain_ollama import ChatOllama

model = ChatOllama(model="llama3.2:1b")

output = model.invoke("What is 49,823 multiplied by 19,283?")

print(output.content)