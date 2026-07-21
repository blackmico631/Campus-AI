from documents.pdf_reader import read_pdf
from documents.chunker import split_text


text = read_pdf(
    "data/documents/assembly/assembly-actualmachine-report.pdf"
)

print("\n===== PDF RAW TEXT =====")
print(repr(text[:2000]))

chunks = split_text(text)

print(f"PDF全文: {len(text)}文字")
print(f"チャンク数: {len(chunks)}")


for i, chunk in enumerate(chunks[:5]):
    print(f"\n===== Chunk {i + 1} =====")
    print(f"文字数: {len(chunk)}")
    print("-" * 40)
    print(chunk)


print("\n\n===== Overlap確認 =====")

for i in range(min(len(chunks) - 1, 4)):

    previous_lines = chunks[i].split("\n")
    next_lines = chunks[i + 1].split("\n")

    print(f"\nChunk {i + 1} の最後の2 unit:")

    for line in previous_lines[-2:]:
        print(repr(line))

    print(f"\nChunk {i + 2} の最初の2 unit:")

    for line in next_lines[:2]:
        print(repr(line))