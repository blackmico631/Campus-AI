from documents.pdf_reader import read_pdf
from documents.chunker import split_text
from documents.retriever import search_chunks


class RAG:
    def __init__(self, file_path: str):
        text = read_pdf(file_path)
        self.chunks = split_text(text)

    def retrieve(self, question: str, top_k: int = 3) -> str:
        results = search_chunks(
            question=question,
            chunks=self.chunks,
            top_k=top_k
        )

        context = "\n\n---\n\n".join(
            chunk for chunk, score in results
        )

        return context