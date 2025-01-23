from PyPDF2 import PdfReader
import docx

def extract_text_from_pdf(file):
    """Extract text from a PDF file."""
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def extract_text_from_docx(file):
    """Extract text from a DOCX file."""
    doc = docx.Document(file)
    text = [paragraph.text for paragraph in doc.paragraphs]
    return "\n".join(text)

def extract_text(file, file_type):
    """Extract text based on file type."""
    if file_type == "pdf":
        return extract_text_from_pdf(file)
    elif file_type == "docx":
        return extract_text_from_docx(file)
    else:
        raise ValueError("Unsupported file type. Please upload a PDF or DOCX file.")
