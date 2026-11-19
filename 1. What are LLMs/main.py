# import necessary module
import requests
import os
from dotenv import load_dotenv

# load secret env credentials
load_dotenv()

# API KEY which created through google AI stuio
API_KEY = os.getenv("GEMINI_API_KEY")
# model ID 
MODEL = "gemini-3.8-flash"

# to ask question in gemini you need its URL
URL = (f"https://generativelanguage.googleapis.com/v1beta/"
       f"models/{MODEL}:generateContent"
      )
# configure https headers
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
    URL, #send your URL
    headers=headers, #confugure https headers
    json=data, # send actual question
    timeout=300 # adjust based on your internet connection
)
# check for response
response.raise_for_status()
# convert result into response
response.json()