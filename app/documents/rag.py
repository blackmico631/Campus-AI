from documents.retriever import search_indexes


class RAG:
    def __init__(self, index_paths: list[str]):
        self.index_paths = index_paths

    def retrieve(
        self,
        question: str,
        top_k: int = 3
    ) -> str:

        results = search_indexes(
            question=question,
            index_paths=self.index_paths,
            top_k=top_k
        )

        context = "\n\n---\n\n".join(
            chunk for chunk, score in results
        )

        return context