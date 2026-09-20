from src.memory import ConversationStore
from src.gemini import generate_reply


# Create the memory store
store = ConversationStore(max_messages=10)


def process_message(user_id, user_message):

    # 1. Get previous conversation
    history = store.get_history(user_id)

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
    return answer