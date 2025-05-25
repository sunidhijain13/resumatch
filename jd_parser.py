from resume_parser import extract_text_from_pdf

def extract_jd_text_from_pdf(file) -> str:
    """Wrapper for JD parsing, reuses resume parser."""
    return extract_text_from_pdf(file)
