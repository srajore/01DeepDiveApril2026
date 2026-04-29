from groq import Groq

from dotenv import load_dotenv

import httpx

load_dotenv()  # Load environment variables from .env file

client = Groq(
     http_client=httpx.Client(verify=False)
)
completion = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
      {
        "role": "user",
        "content": "Write a poem on Narendra Modi?"
      }
    ],
    temperature=1,
    top_p=1,
    stream=True,
    stop=None
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")
