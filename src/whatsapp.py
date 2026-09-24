import os
import requests

from dotenv import load_dotenv

load_dotenv()

META_ACCESS_TOKEN = os.getenv("META_ACCESS_TOKEN")
META_PHONE_NUMBER_ID = os.getenv("META_PHONE_NUMBER_ID")

if not META_ACCESS_TOKEN:
    raise ValueError("META_ACCESS_TOKEN is missing")

if not META_PHONE_NUMBER_ID:
    raise ValueError("META_PHONE_NUMBER_ID is missing")


def send_whatsapp_message(to, message):

    url = (
        f"https://graph.facebook.com/v25.0/"
        f"{META_PHONE_NUMBER_ID}/messages"
    )

    headers = {
        "Authorization": f"Bearer {META_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    data = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {
            "body": message
        }
    }

    response = requests.post(
        url,
        headers=headers,
        json=data
    )

    print("Meta response:", response.status_code)
    print(response.text)

    response.raise_for_status()

    return response.json()