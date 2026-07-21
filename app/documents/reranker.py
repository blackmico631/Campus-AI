from ollama import chat
from config import CHAT_MODEL
import re

def score_chunk(
    question: str,
    chunk: str
) -> float:

    prompt = f"""
あなたはRAG検索システムのRe-rankerです。

ユーザーの質問に対して、以下の資料チャンクが
「質問へ直接回答するための根拠としてどれほど有用か」
を0から10で厳密に評価してください。

【質問】
{question}

【資料チャンク】
{chunk}

以下の基準で評価してください。

0:
質問と無関係。

1～3:
同じ分野について書かれているだけで、
質問そのものへの回答にはほとんど役立たない。

4～6:
質問に関連する情報を含むが、
直接的な回答には不十分。

7～8:
質問への回答にかなり役立つ情報を含む。

9:
質問に直接答える重要な情報を含む。

10:
このチャンクだけで質問に十分かつ直接的に回答できる。

重要:
質問と同じ単語が含まれているだけでは高得点にしないでください。
「質問に直接答えるための根拠になるか」を最優先してください。

0から10までの数値だけを出力してください。
説明や理由は一切出力しないでください。

出力例:
7
"""

    response = chat(
        model=CHAT_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    content = response.message.content.strip()

    match = re.search(r"\b(?:10(?:\.0+)?|[0-9](?:\.\d+)?)\b", content)

    if match:
        return float(match.group())

    return 0.0


def rerank(
    question: str,
    results: list[dict],
    top_k: int = 3
) -> list[dict]:

    reranked_results = []

    for result in results:

        rerank_score = score_chunk(
            question=question,
            chunk=result["chunk"]
        )

        new_result = result.copy()
        new_result["rerank_score"] = rerank_score

        reranked_results.append(new_result)

    reranked_results.sort(
        key=lambda x: x["rerank_score"],
        reverse=True
    )

    return reranked_results[:top_k]