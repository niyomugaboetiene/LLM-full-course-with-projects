# Simple terminal based AI chatbots with openrouter API
# the model used is inclusionAI: Ling 3.2 Flash is free 

import os
from dotenv import load_dotenv
import requests


load_dotenv()

API_KEY = os.getenv("OPEN_ROUTER_API_KEY")

MODEL = "inclusionai/ling-3.2-flash:free"
URL = "https://openrouter.ai/api/v1/chat/completions"

header = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

user_message = input("You: ")

messages = [
    {
        "role": "user",
        "content": user_message
    }
]

data = {
    "model": MODEL,
    "messages": messages
}

response = requests.post(
    URL,
    json=data,
    headers=header,    
)

response.raise_for_status()
# result = response.json()
# print(result)
print(response.status_code)
print(response.text)