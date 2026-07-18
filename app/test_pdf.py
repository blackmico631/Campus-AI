from documents.pdf_reader import read_pdf
from ai.client import CampusAI

# PDFを読み込む
text = read_pdf("data/documents/アセンブリ言語実機演習レポート.pdf")

# CampusAIを起動
ai = CampusAI()

# PDFの内容を含めて質問する
question = """
以下は大学の講義資料です。
資料の内容に基づいて、重要なポイントを3つ説明してください。

【講義資料】
""" + text

answer = ai.ask(question)

print(answer)