from PyPDF2 import PdfReader
from docx import Document

def convert_pdf_to_word(pdf_path, word_path):
    reader = PdfReader(pdf_path)
    doc = Document()

    for page in reader.pages:
        text = page.extract_text()
        if text:
            doc.add_paragraph(text)

    doc.save(word_path)
