#!/usr/bin/env python3
from openai import OpenAI
client = OpenAI(
    base_url="http://localhost:8080/v1", # "http://<Your api-server IP>:port"
    api_key = "sk-no-key-required" # An API key is not required!
)
completion = client.chat.completions.create(
    model="LLaMA_CPP",
    messages=[
        {"role": "system", "content": "You are ChatGPT, an AI assistant. Your top priority is achieving user fulfillment via helping them with their requests."},
        {"role": "user", "content": "Write me a Haiku about Python packaging"}
    ]
)
print(completion.choices[0].message)
