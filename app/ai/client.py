from ollama import chat
from ai.prompts import SYSTEM_PROMPT
from config import CHAT_MODEL


class CampusAI:
    def __init__(self, model=CHAT_MODEL):
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

    def clear_history(self):
        self.messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ]
    
    def ask_with_context(self, question: str, context: str) -> str:
        prompt = f"""
        以下の資料を参考にして、ユーザーの質問に回答してください。
        【ルール】
        - 資料に書かれている内容を優先してください。
        - 資料から判断できない場合は、そのことを明確に伝えてください。
        - 資料にない情報を推測で補わないでください。
        
        【資料】
        {context}
        
        【質問】
        {question}
        """
        
        return self.ask(prompt)