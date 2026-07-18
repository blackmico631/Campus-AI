from pathlib import Path


class SubjectManager:
    def __init__(self, indexes_dir: str = "data/indexes"):
        self.indexes_dir = Path(indexes_dir)
        self.current_subject = None

    def get_subjects(self) -> list[str]:
        if not self.indexes_dir.exists():
            return []

        return [
            path.name
            for path in self.indexes_dir.iterdir()
            if path.is_dir()
        ]

    def select_subject(self, subject: str) -> bool:
        subject_path = self.indexes_dir / subject

        if subject_path.exists() and subject_path.is_dir():
            self.current_subject = subject
            return True

        return False

    def get_index_files(self) -> list[str]:
        if self.current_subject is None:
            return []

        subject_path = self.indexes_dir / self.current_subject

        return [
            str(path)
            for path in subject_path.glob("*.json")
        ]