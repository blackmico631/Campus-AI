import math

from documents.embedder import create_embedding

import json

from pathlib import Path


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


def search_index(
    question: str,
    index_path: str,
    top_k: int = 3
) -> list[dict]:

    filename = Path(index_path).with_suffix(".pdf").name

    # 保存済みインデックスを読み込む
    with open(index_path, "r", encoding="utf-8") as f:
        index_data = json.load(f)

    # 質問だけEmbedding
    question_embedding = create_embedding(question)

    results = []

    for item in index_data:
        similarity = cosine_similarity(
            question_embedding,
            item["embedding"]
        )

        results.append(
            {
                "chunk": item["chunk"],
                "score": similarity,
                "file": item["file"],
                "page": item["page"]
            }
        )

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return results[:top_k]


def search_indexes(
    question: str,
    index_paths: list[str],
    top_k: int = 3
) -> list[dict]:

    results = []

    for index_path in index_paths:
        results.extend(
            search_index(
                question=question,
                index_path=index_path,
                top_k=top_k
            )
        )

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return results[:top_k]