from ai.client import CampusAI
from documents.rag import RAG
from documents.subject_manager import SubjectManager


ai = CampusAI()

manager = SubjectManager()

manager.select_subject("assembly")

index_files = manager.get_index_files()

rag = RAG(index_files)

question = "この講義資料の重要なポイントを説明してください"

context = rag.retrieve(question)

answer = ai.ask_with_context(
    question=question,
    context=context
)

print(f"科目: {manager.current_subject}")
print(f"質問: {question}")
print()
print("CampusAI:")
print(answer)