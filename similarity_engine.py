import numpy as np
import faiss

def get_embedding(text: str) -> np.ndarray:
    """
    Mock embedding generator for development (no OpenAI needed).
    Generates deterministic pseudo-embeddings based on input text.
    """
    np.random.seed(abs(hash(text)) % (2**32))  # Consistent seed per input
    return np.random.rand(1536).astype("float32")  # Mimics OpenAI embedding size

def get_similarity_score(resume_text: str, jd_text: str) -> float:
    """
    Computes a mock cosine similarity score between resume and JD using FAISS.
    """
    resume_emb = get_embedding(resume_text)
    jd_emb = get_embedding(jd_text)

    dim = len(resume_emb)
    index = faiss.IndexFlatL2(dim)
    index.add(np.array([jd_emb]))

    D, I = index.search(np.array([resume_emb]), k=1)
    distance = D[0][0]

    similarity = 1 / (1 + distance)
    return round(similarity * 100, 2)
