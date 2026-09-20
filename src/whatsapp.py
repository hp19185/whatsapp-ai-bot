import os

from dotenv import load_dotenv
from twilio.rest import Client


load_dotenv()


TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER")


if not TWILIO_ACCOUNT_SID:
    raise ValueError("TWILIO_ACCOUNT_SID is missing")

if not TWILIO_AUTH_TOKEN:
    raise ValueError("TWILIO_AUTH_TOKEN is missing")

if not TWILIO_WHATSAPP_NUMBER:
    raise ValueError("TWILIO_WHATSAPP_NUMBER is missing")


client = Client(
    TWILIO_ACCOUNT_SID,
    TWILIO_AUTH_TOKEN
)


def send_whatsapp_message(to, message):

    result = client.messages.create(
        from_=TWILIO_WHATSAPP_NUMBER,
        to=to,
        body=message
    )

    return result.sid

if __name__ == "__main__":

    sid = send_whatsapp_message(
        "whatsapp:+919601451273",
        "Hello from my Python WhatsApp bot!"
    )

    print("Message SID:", sid)