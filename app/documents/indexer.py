import json
from pathlib import Path

from documents.pdf_reader import read_pdf_pages
from documents.chunker import split_pages
from documents.embedder import create_embedding


def create_index(pdf_path: str, index_path: str):
    filename = Path(pdf_path).name

    pages = read_pdf_pages(pdf_path)
    chunks = split_pages(pages)

    index_data = []

    print(f"チャンク数: {len(chunks)}")
    print("Embeddingを作成しています...")

    for i, chunk_data in enumerate(chunks):
        embedding = create_embedding(
            chunk_data["chunk"]
        )

        index_data.append(
            {
                "chunk": chunk_data["chunk"],
                "page": chunk_data["page"],
                "file": filename,
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
            ensure_ascii=False,
            indent=2
        )
        
    print(f"インデックスを保存しました: {index_path}")