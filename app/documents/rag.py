from documents.retriever import search_indexes
from documents.reranker import rerank


class RAG:
    def __init__(self, index_paths: list[str]):
        self.index_paths = index_paths

    def retrieve(
        self,
        question: str,
        candidate_k: int = 10,
        top_k: int = 3
    ) -> dict:

        results = search_indexes(
            question=question,
            index_paths=self.index_paths,
            top_k=candidate_k
        )
        results = rerank(
            question=question,
            results=results,
            top_k=top_k
        )

        print("\n========== DEBUG ==========")

        for i, result in enumerate(results, start=1):
            print(f"\nChunk {i}")
            print(f"File : {result['file']}")
            print(f"Page : {result['page']}")
            print(f"Embedding Score : {result['score']:.4f}")
            print(f"Re-rank Score   : {result['rerank_score']:.1f}")
            print("----------------------")
            print(result["chunk"][:300])

        print("===========================\n")

        context = "\n\n---\n\n".join(
            result["chunk"] for result in results
        )

        return {
            "context": context,
            "results": results
        }