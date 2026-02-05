import pdfplumber
from docx import Document

def extract_text(file, filename):

    if filename.endswith(".pdf"):
        text = ""
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
        return text

    elif filename.endswith(".docx"):
        doc = Document(file)
        return "\n".join(p.text for p in doc.paragraphs)

    elif filename.endswith(".txt"):
        return file.read().decode("utf-8")

    return ""
