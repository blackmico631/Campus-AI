# CampusAI

> **A local AI assistant for university students.**

CampusAI は、大学講義のPDF資料を読み込み、
資料に基づいた回答を生成するローカルRAGアプリケーションです。

特徴

- 🔒 完全ローカルで動作
- 📚 科目ごとの資料管理
- 🔍 Semantic Search + Re-ranking
- 🤖 Qwen3による回答生成
- 📄 参考資料を自動表示

---

## 主な機能

- PDFの読み込み
- 科目ごとの資料管理
- Embeddingによる意味検索
- Re-rankingによる検索精度向上
- RAGによる回答生成
- 回答に参考資料を表示
- CLIによる操作

---

## 使用技術

- Python
- Ollama
- Qwen3
- pypdf
- JSON
- Git

---

## ディレクトリ構成

```text
CampusAI/
├── app/
│   ├── ai/
│   ├── documents/
│   ├── main.py
│   └── config.py
├── data/
│   ├── documents/
│   └── indexes/
└── README.md
```

---

## セットアップ

### 1. 仮想環境

```bash
python -m venv .venv
```

### 2. 有効化

Linux / WSL

```bash
source .venv/bin/activate
```

Windows

```powershell
.venv\Scripts\activate
```

### 3. ライブラリ

```bash
pip install -r requirements.txt
```

### 4. Ollama起動

```bash
ollama serve
```

### 5. モデル取得

```bash
ollama pull qwen3:8b
```

---

## 使い方

起動

```bash
python app/main.py
```

科目一覧

```text
/subjects
```

科目選択

```text
/subject assembly
```

資料追加

```text
/index assembly
```

質問

```text
アセンブリ言語の存在意義は？
```

---

## 開発履歴

### v1.0.0

- CLI完成
- PDF読み込み
- RAG
- Semantic Search
- Re-ranking
- Chunk改善
- 参考資料表示

---

## 今後の予定

- Markdown出力
- Web UI
- 学習履歴
- テスト生成
- ノート管理
- 長期記憶

---

## ライセンス

MIT License
