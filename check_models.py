import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load your .env variables
load_dotenv()

# Get API key from .env file
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    print("❌ API key not found! Add it to your .env file.")
    exit()

# Configure API
genai.configure(api_key=api_key)

# List all available models
print("✅ Models available for your account:\n")
for m in genai.list_models():
    print(m.name)
