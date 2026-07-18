from ai.client import CampusAI
from documents.rag import RAG


ai = CampusAI()

rag = RAG(
    "data/documents/アセンブリ言語実機演習レポート.pdf"
)

question = "LEDの点灯に関する考察について説明してください"

context = rag.retrieve(question)

answer = ai.ask_with_context(
    question=question,
    context=context
)

print(f"質問: {question}")
print()
print("CampusAI:")
print(answer)