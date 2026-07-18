import math

from documents.embedder import create_embedding


def cosine_similarity(vector_a: list[float], vector_b: list[float]) -> float:
    dot_product = sum(a * b for a, b in zip(vector_a, vector_b))

    magnitude_a = math.sqrt(sum(a * a for a in vector_a))
    magnitude_b = math.sqrt(sum(b * b for b in vector_b))

    if magnitude_a == 0 or magnitude_b == 0:
        return 0.0

    return dot_product / (magnitude_a * magnitude_b)


def search_chunks(
    question: str,
    chunks: list[str],
    top_k: int = 3
) -> list[tuple[str, float]]:

    question_embedding = create_embedding(question)

    results = []

    for chunk in chunks:
        chunk_embedding = create_embedding(chunk)

        similarity = cosine_similarity(
            question_embedding,
            chunk_embedding
        )

        results.append((chunk, similarity))

    results.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return results[:top_k]