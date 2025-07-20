# import os
# import json
# from dotenv import load_dotenv
# import requests

# load_dotenv()
# API_KEY = os.getenv("GIMINI_API_KEY")

# def get_gimini_response(prompt):
#     url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"
#     headers = 'content-type: application/json'
#     dictionary ={'content':[{'parts':[{"text":prompt}]}]}

#     response = requests.post (url, headers={'Content-Type': headers}, json=dictionary)
#     result = response.json()
#     print(result)
#     return result['condidates'][0]['content']['parts'][0]['text']

# while True:
#     user_input = input("Enter your prompt (or 'exit' to quit): ")
#     if user_input.lower() == 'exit':
#         break
#     try:
#         reply = get_gimini_response(user_input)
#         print("Bot:", reply)
#     except Exception as e:
#         print('An error occurred:', e)

import os
from dotenv import load_dotenv
import requests

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("GIMINI_API_KEY")

def get_gimini_response(prompt):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"
    
    headers = {'Content-Type': 'application/json'}
    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    response = requests.post(url, headers=headers, json=payload)
    result = response.json()
    
    return result['candidates'][0]['content']['parts'][0]['text']

# Interactive loop
while True:
    user_input = input("Enter your prompt (or 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break
    try:
        reply = get_gimini_response(user_input)
        print("Bot:", reply)
    except Exception as e:
        print("An error occurred:", e)
