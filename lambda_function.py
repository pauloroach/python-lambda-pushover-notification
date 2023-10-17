import json
import requests
import os

def lambda_handler(event, context):
    message = "CloudWatch Alarm triggered: " + json.dumps(event)
    send_pushover_notification(message)

def send_pushover_notification(message):
    user_key = 'xxxxxxxx'
    api_token = 'xxxxxxxxx'
    url = 'https://api.pushover.net/1/messages.json'
    data = {
        'token': api_token,
        'user': user_key,
        'message': message,
    }
    r = requests.post(url, data=data)
    if r.status_code == 200:
        print("Notification sent successfully.")
    else:
        print(f"Failed to send notification. Status code: {r.status_code}")