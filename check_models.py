import os

import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv(override=True)

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise SystemExit("Missing GOOGLE_API_KEY. Set it in your environment or in a .env file.")

genai.configure(api_key=api_key)

print("Available models for your API key:")
for m in genai.list_models():
    if "generateContent" in m.supported_generation_methods:
        print(f"- {m.name}")