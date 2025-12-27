from collections import defaultdict, deque
from config import MAX_HISTORY, SYSTEM_PROMPT

class MemoryStore:
    def __init__(self):
        self.store = defaultdict(
            lambda: deque(
                [{"role": "system", "content": SYSTEM_PROMPT}],
                maxlen=MAX_HISTORY * 2 + 1
            )
        )

    def add_user_message(self, user_id: int, text: str):
        self.store[user_id].append({"role": "user", "content": text})

    def add_assistant_message(self, user_id: int, text: str):
        self.store[user_id].append({"role": "assistant", "content": text})

    def get_messages(self, user_id: int):
        return list(self.store[user_id])

    def clear(self, user_id: int):
        self.store[user_id].clear()
        self.store[user_id].append(
            {"role": "system", "content": SYSTEM_PROMPT}
        )
