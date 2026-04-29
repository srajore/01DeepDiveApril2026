import anthropic

from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

client = anthropic.Anthropic()

message = client.messages.create(
  model="claude-haiku-4-5-20251001",
  max_tokens=1024,
  messages=[{
    "role": "user",
    "content": "What is the capital of USA?"
  }]
)
print(message.content[0].text)