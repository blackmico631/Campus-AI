from pypdf import PdfReader


def read_pdf(file_path: str) -> str:
    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def read_pdf_pages(file_path: str) -> list[dict]:
    reader = PdfReader(file_path)

    pages = []

    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            pages.append(
                {
                    "page": i + 1,
                    "text": text
                }
            )

    return pages