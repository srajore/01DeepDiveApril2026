from openai import OpenAI

from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file


client = OpenAI()


response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of India?"},
    ],
)

print(response.choices[0].message.content)