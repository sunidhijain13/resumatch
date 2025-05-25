import pdfplumber

def extract_text_from_pdf(file) -> str:
    """Extracts text from a PDF file using pdfplumber."""
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text.strip()
