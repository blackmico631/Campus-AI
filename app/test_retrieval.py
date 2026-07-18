from documents.pdf_reader import read_pdf
from documents.chunker import split_text
from documents.retriever import search_chunks


text = read_pdf("data/documents/アセンブリ言語実機演習レポート.pdf")

chunks = split_text(text)

question = "LEDの点灯に関する考察について説明してください"

results = search_chunks(
    question=question,
    chunks=chunks,
    top_k=3
)

print(f"質問: {question}")

for i, (chunk, score) in enumerate(results):
    print(f"\n===== 検索結果 {i + 1} =====")
    print(f"類似度: {score:.4f}")
    print(chunk[:500])