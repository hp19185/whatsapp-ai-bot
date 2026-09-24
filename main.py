from fastapi import FastAPI, Request, HTTPException, Response
from src.bot import process_message

app = FastAPI()
@app.get("/")
def home():
    return {
        "message": "WhatsApp AI Bot is running!"
    }

@app.get("/webhook")
async def verify_webhook(request: Request):

    params = request.query_params

    mode = params.get("hub.mode")
    token = params.get("hub.verify_token")
    challenge = params.get("hub.challenge")

    if (
        mode == "subscribe"
        and token == "wchatbot_verify_2026"
    ):
        return Response(
            content=challenge,
            media_type="text/plain"
        )

    raise HTTPException(
        status_code=403,
        detail="Webhook verification failed"
    )
@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()

    try:
        value = data["entry"][0]["changes"][0]["value"]

        # Ignore webhook events that are not incoming messages
        messages = value.get("messages")

        if not messages:
            print("Webhook event received without messages. Ignoring.")
            return {"status": "ok"}

        message = messages[0]

        # We currently handle text messages only
        if message.get("type") != "text":
            print("Non-text message received. Ignoring.")
            return {"status": "ok"}

        user_id = message["from"]
        user_message = message["text"]["body"]

        print("User:", user_id)
        print("Message:", user_message)

        process_message(
            user_id,
            user_message
        )

        return {
            "status": "ok"
        }

    except Exception as e:
        print("Webhook error:", e)

        # Still acknowledge the webhook
        return {
            "status": "error"
        }