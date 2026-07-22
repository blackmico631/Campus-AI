from documents.retriever import search_indexes


# 検索対象のインデックス
index_paths = [
    "data/indexes/assembly/assembly00.json",
    "data/indexes/assembly/assembly06.json",
    "data/indexes/assembly/assembly-actualmachine-report.json"
]


# テスト用の質問
question = "アセンブリ言語の存在意義は？"


# 検索
results = search_indexes(
    question=question,
    index_paths=index_paths,
    top_k=3
)


# 結果表示
print("\n===== 検索結果 =====\n")

for i, result in enumerate(results, start=1):
    print(f"===== Chunk {i} =====")
    print(f"File : {result['file']}")
    print(f"Page : {result['page']}")
    print(f"Score: {result['score']:.4f}")
    print("--------------------")
    print(result["chunk"][:300])
    print()