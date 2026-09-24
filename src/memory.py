from typing import Dict, List


class ConversationStore:
    def __init__(self, max_messages: int = 10):
        self.max_turns = max_messages
        self.conversations: Dict[str, List[dict]] = {}

    def get_history(self, user_id: str) -> List[dict]:
        return self.conversations.get(user_id, [])

    def add_message(self, user_id: str, role: str, content: str) -> None:
        if user_id not in self.conversations:
            self.conversations[user_id] = []

        self.conversations[user_id].append({
            "role": role,
            "content": content
        })

        self.conversations[user_id] = (
            self.conversations[user_id][-self.max_turns:]
        )

        print("\n========== MEMORY ==========")
        print("User ID:", user_id)
        print("Messages stored:", len(self.conversations[user_id]))
        print("History:")
        print(self.conversations[user_id])
        print("============================\n")
    def clear_history(self, user_id: str) -> None:
        self.conversations.pop(user_id, None)