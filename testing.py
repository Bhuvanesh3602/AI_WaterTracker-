import requests
import json
import os

import dotenv

dotenv.load_dotenv()
# ✅ Store your Gemini API key safely (replace with your actual key)
API_KEY = os.getenv("GEMINI_API_KEY")  # Best practice — set as environment variable
# If you want to hardcode temporarily (not recommended), uncomment below:
# API_KEY = "your_api_key_here"

url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"

headers = {
    "Content-Type": "application/json",
    "x-goog-api-key": API_KEY
}

data = {
    "contents": [
        {
            "parts": [
                {"text": "Explain how AI works in a few words"}
            ]
        }
    ]
}

response = requests.post(url, headers=headers, data=json.dumps(data))

# Print response
if response.status_code == 200:
    result = response.json()
    print("✅ Response:")
    print(json.dumps(result, indent=2))
else:
    print("❌ Error:", response.status_code, response.text)
