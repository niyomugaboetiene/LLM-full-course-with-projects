import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = "gemini-3.8-flash"

URL = (f"https://generativelanguage.googleapis.com/v1beta/"
       f"models/{MODEL}:generateContent"
      )
headers = {
    "Content-Type": "application/json",
    "x-goog-api-key": API_KEY
}

question = "Hello Can you explain LLM from scratch for beginners"

# create json structure that GEMINI can understanda
data = {
    "contents": [
        {
            "role": "user",
            "parts": [
                {
                    "text": question
                }
            ]
        }
    ]
}

response = requests.post(
    URL,
    headers=headers,
    json=data,
    timeout=60
)
# check for response
response.raise_for_status()
# convert result into response
response.json()