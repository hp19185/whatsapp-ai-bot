import os
import time

from dotenv import load_dotenv
from google import genai


load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is missing")

client = genai.Client(api_key=GEMINI_API_KEY)


def generate_reply(user_message, conversation_history):

    contents = []

    for message in conversation_history:
        contents.append({
            "role": message["role"],
            "parts": [
                {
                    "text": message["content"]
                }
            ]
        })

    contents.append({
        "role": "user",
        "parts": [
            {
                "text": user_message
            }
        ]
    })

    for attempt in range(3):

        try:
            response = client.models.generate_content(
                model="gemini-3.5-flash",
                contents=contents,
                config={
                    "system_instruction": (
                        "Answer in exactly one line. "
                        "Keep the answer concise and do not use line breaks."
                    )
                }
            )

            return response.text

        except Exception as e:

            print(f"Gemini error: {e}")

            if attempt < 2:
                wait_time = 2 ** attempt
                print(f"Retrying in {wait_time} seconds...")
                time.sleep(wait_time)

            else:
                return "Sorry, Gemini is temporarily unavailable. Please try again in a moment."