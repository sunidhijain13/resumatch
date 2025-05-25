from keybert import KeyBERT

kw_model = KeyBERT(model='all-MiniLM-L6-v2')

def extract_keywords(text, top_n=10):
    """Extract keywords from input text using KeyBERT"""
    keywords = kw_model.extract_keywords(text, top_n=top_n, stop_words='english')
    return [kw[0] for kw in keywords]

def find_missing_keywords(resume_text, jd_text, top_n=10):
    jd_keywords = extract_keywords(jd_text, top_n=top_n)
    missing_keywords = [kw for kw in jd_keywords if kw.lower() not in resume_text.lower()]
    return missing_keywords
