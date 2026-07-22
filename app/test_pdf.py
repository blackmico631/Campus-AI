from documents.pdf_reader import read_pdf_pages
from documents.chunker    import split_pages

pages = read_pdf_pages(
    "data/documents/assembly/assembly06.pdf"
)

print(pages[0])


chunks = split_pages(pages)

print(chunks[0])