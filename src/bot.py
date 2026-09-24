from src.memory import ConversationStore
from src.gemini import generate_reply
from src.whatsapp import send_whatsapp_message


# Create the memory store
store = ConversationStore(max_messages=10)

def process_message(user_id, user_message):

    # 1. Get previous conversation
    history = store.get_history(user_id)

    print("\n========== LIVE MEMORY ==========")
    print("user_id:", user_id)
    print("max_messages:", store.max_turns)
    print("current_messages:", len(history))
    print("history:", history)
    print("=================================\n")

    # 2. Ask Gemini using previous conversation + new message
    answer = generate_reply(
        user_message,
        history
    )

    # 3. Store the user's new message
    store.add_message(
        user_id,
        "user",
        user_message
    )

    # 4. Store Gemini's response
    store.add_message(
        user_id,
        "model",
        answer
    )

    # 5. Return the response
    send_whatsapp_message(
        user_id,
        answer
    )

    return answer