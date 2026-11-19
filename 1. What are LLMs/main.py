# import necessary module
import requests
import os
from dotenv import load_dotenv

# load secret env credentials
load_dotenv()

# API KEY which created through OpenAI stuio
API_KEY = os.getenv("OPENAI_API_KEY")

# to ask question in ChatGPT you need its URL
URL = "https://api.openai.com/v1/responses"
# configure https headers
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

question = "Hello Can you explain LLM from scratch for beginners"

# create json structure that ChatGPT can understand
# data = {
#     "contents": [
#         {
#             "role": "user",
#             "parts": [
#                 {
#                     "text": question
#                 }
#             ]
#         }
#     ]
# }
data = {
    "model": "gpt-4.1-mini",
    "input": question
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
print(response.json())