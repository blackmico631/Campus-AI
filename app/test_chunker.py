from documents.pdf_reader import read_pdf
from documents.chunker import split_text


text = read_pdf("data/documents/アセンブリ言語実機演習レポート.pdf")

chunks = split_text(text)

print(f"PDF全文: {len(text)}文字")
print(f"チャンク数: {len(chunks)}")

for i, chunk in enumerate(chunks[:3]):
    print(f"\n===== Chunk {i + 1} =====")
    print(chunk[:300])