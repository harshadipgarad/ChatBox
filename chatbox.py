import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")
url = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

print("=" * 50)
print("AI Chatbot is now running! (Type 'exit' to quit)")
print("=" * 50 + "\n")

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "exit":
        print("Bot: Goodbye! Have a great day.")
        break
        
    if not user_input.strip():
        continue
        
    data = {
        "model": "deepseek/deepseek-chat", # You can also use gpt-4o-mini or claude
        "messages": [
            {"role": "user", "content": user_input}
        ]
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        
        if response.status_code == 200:
            response_json = response.json()
            # Extracting only the main reply message from the response
            bot_message = response_json['choices'][0]['message']['content']
            print(f"Bot: {bot_message}")
            print("-" * 50 + "\n")
        else:
            print(f"Error: {response.status_code} - {response.text}\n")
            
    except Exception as e:
        print(f"A technical error occurred: {e}\n")