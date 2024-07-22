# brainshop_helper.py
import requests
import json
from datetime import datetime

def get_brainshop_response(api_key, bot_id, user_input, user_id):
    url = f"http://api.brainshop.ai/get?bid={bot_id}&key={api_key}&uid={user_id}&msg={user_input}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("cnt")
    else:
        return "Sorry, I couldn't process your request."

def save_response(user_input, response, filename="responses.json"):
    data = {
        "timestamp": datetime.now().isoformat(),
        "user_input": user_input,
        "response": response
    }
    try:
        with open(filename, "a") as file:
            file.write(json.dumps(data) + "\n")
    except Exception as e:
        print(f"Failed to save response: {e}")

def ping_brainshop_api(api_key, bot_id):
    url = f"http://api.brainshop.ai/get?bid={bot_id}&key={api_key}&uid=test_ping&msg=ping"
    response = requests.get(url)
    if response.status_code == 200:
        return "Online"
    else:
        return "Offline"
