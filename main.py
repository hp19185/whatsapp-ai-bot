from fastapi import FastAPI, Form
from src.bot import process_message

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "WhatsApp AI Bot is running!"
    }


@app.post("/webhook")
def webhook(
    From: str = Form(...),
    Body: str = Form(...)
):
    answer = process_message(
        From,
        Body
    )

    return {
        "reply": answer
    }