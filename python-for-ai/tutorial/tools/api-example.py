# app.py
from dotenv import load_dotenv
import os
import requests

# Load environment variables
load_dotenv()
# get API key
API_KEY = os.environ.get("OPENAI_API_KEY")

if not API_KEY:
    print("Please set OPENAI_API_KEY in .env file")
    exit(1)

# Use the API key
headers = {"Authorization": f"Bearer {API_KEY}"}
# Make your API calls...

headers

"""Quick tips
Load early: Put load_dotenv() at the start of your program
Use defaults: os.environ.get('PORT', '8000')
Check your .gitignore: Make sure .env is listed
Keep it simple: Only put configuration that changes"""
