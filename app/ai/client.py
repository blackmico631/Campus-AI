from ollama import chat
from ai.prompts import SYSTEM_PROMPT

class CampusAI:
    def __init__(self, model="qwen3:8b"):
        self.model = model
        self.messages = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    }
]

    def ask(self, message: str) -> str:
        self.messages.append(
            {
                "role": "user",
                "content": message
            }
        )

        response = chat(
            model=self.model,
            messages=self.messages
        )

        answer = response.message.content

        self.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

        return answer