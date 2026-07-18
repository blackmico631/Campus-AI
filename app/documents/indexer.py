import json
from pathlib import Path

from documents.pdf_reader import read_pdf
from documents.chunker import split_text
from documents.embedder import create_embedding


def create_index(pdf_path: str, index_path: str):
    # PDFからテキストを抽出
    text = read_pdf(pdf_path)

    # テキストをChunkに分割
    chunks = split_text(text)

    index_data = []

    print(f"チャンク数: {len(chunks)}")
    print("Embeddingを作成しています...")

    for i, chunk in enumerate(chunks):
        embedding = create_embedding(chunk)

        index_data.append(
            {
                "chunk": chunk,
                "embedding": embedding
            }
        )

        print(f"{i + 1}/{len(chunks)} 完了")

    # 保存先フォルダがなければ作成
    Path(index_path).parent.mkdir(
        parents=True,
        exist_ok=True
    )

    # JSONとして保存
    with open(index_path, "w", encoding="utf-8") as f:
        json.dump(
            index_data,
            f,
            ensure_ascii=False
        )

    print(f"インデックスを保存しました: {index_path}")