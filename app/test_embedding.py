from documents.embedder import create_embedding


text = "確率分布とは何ですか？"

embedding = create_embedding(text)

print(f"ベクトルの次元数: {len(embedding)}")
print("最初の10個:")
print(embedding[:10])