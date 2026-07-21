from pathlib import Path

from documents.indexer import create_index


class DocumentManager:
    def __init__(
        self,
        documents_dir: str = "data/documents",
        indexes_dir: str = "data/indexes"
    ):
        self.documents_dir = Path(documents_dir)
        self.indexes_dir = Path(indexes_dir)

    def add_document(
        self,
        subject: str,
        filename: str
    ) -> str:

        pdf_path = (
            self.documents_dir
            / subject
            / filename
        )

        if not pdf_path.exists():
            return (
                f"PDFが見つかりません: "
                f"{pdf_path}"
            )

        if pdf_path.suffix.lower() != ".pdf":
            return "PDFファイルを指定してください。"

        index_dir = (
            self.indexes_dir
            / subject
        )

        index_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        index_path = (
            index_dir
            / f"{pdf_path.stem}.json"
        )

        create_index(
            pdf_path=str(pdf_path),
            index_path=str(index_path)
        )

        return (
            f"資料「{filename}」を"
            f"科目「{subject}」に登録しました。"
        )

    def index_new_documents(self, subject: str) -> list[str]:
        subject_documents_dir = self.documents_dir / subject
        subject_indexes_dir = self.indexes_dir / subject
        
        if not subject_documents_dir.exists():
            return []
            
        subject_indexes_dir.mkdir(
                parents=True,
                exist_ok=True
        )
            
        registered_files = []

        print("DEBUG PDFs:", list(subject_documents_dir.glob("*.pdf")))

        for pdf_path in subject_documents_dir.glob("*.pdf"):

            index_path = (
                subject_indexes_dir
                / f"{pdf_path.stem}.json"
            )
            
            print(f"DEBUG: {pdf_path.name} -> {index_path.exists()}")

            # すでにJSONが存在する場合はスキップ
            if index_path.exists():
                print(f"✓ {pdf_path.name} 登録済み")
                continue

            print(f"→ {pdf_path.name} を登録します")

            create_index(
            pdf_path=str(pdf_path),
            index_path=str(index_path)
            )

            registered_files.append(pdf_path.name)
            
        return registered_files