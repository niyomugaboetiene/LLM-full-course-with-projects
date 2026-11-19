import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = "gemini-2.5-flash"

URL = (f"https://generativelanguage.googleapis.com/v1beta/"
       f"models/{MODEL}:generateContent"
      )
headers = {
    "C"
}