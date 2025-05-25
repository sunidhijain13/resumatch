import streamlit as st
from io import BytesIO

from resume_parser import extract_text_from_pdf
from jd_parser import extract_jd_text_from_pdf
from similarity_engine import get_similarity_score
from gpt_rewriter import suggest_resume_bullets
from keyword_matcher import find_missing_keywords
from pdf_utils import generate_pdf

st.set_page_config(page_title="ResuMatch.ai", layout="wide")
st.title("📄 ResuMatch.ai – Resume Optimizer")
st.markdown("AI-powered resume–job alignment, bullet rewrites, and keyword gap analysis.")

# ---------------- Sidebar ---------------- #
st.sidebar.title("⚙️ About This Tool")
st.sidebar.markdown("""
I made this tool to help job seekers:
- Analyze how well their resume matches a job description
- Get improved bullet suggestions using AI (mocked for development)

Built with love (and with professionalism of course 😬) by [Sunidhi Jain](https://www.linkedin.com/in/sunidhijain13)
""")

# ---------------- Upload Section ---------------- #
st.divider()
st.subheader("📤 Upload Files")

col1, col2 = st.columns(2)

with col1:
    resume_file = st.file_uploader("📄 Upload Resume (PDF)", type=["pdf"])
    resume_text = None
    if resume_file:
        resume_text = extract_text_from_pdf(BytesIO(resume_file.read()))
        st.text_area("✍️ Resume Content", resume_text, height=300)

with col2:
    jd_file = st.file_uploader("📝 Upload Job Description (PDF)", type=["pdf"])
    jd_text = None
    if jd_file:
        jd_text = extract_jd_text_from_pdf(BytesIO(jd_file.read()))
        st.text_area("📃 Job Description Content", jd_text, height=300)

# ---------------- AI Analysis Section ---------------- #
st.divider()
st.subheader("🧠 Match Analysis & Suggestions")

if resume_file and jd_file:
    if st.button("🚀 Analyze Resume–JD Match"):
        with st.spinner("🔍 Calculating Match Score..."):
            score = get_similarity_score(resume_text, jd_text)
            st.markdown(f"### ✅ Match Score: `{score}%`")

        with st.spinner("💡 Generating AI Resume Suggestions..."):
            suggestions = suggest_resume_bullets(resume_text, jd_text, use_mock=True)
            st.subheader("✨ AI-Optimized Bullet Points")
            st.markdown(suggestions)

            # Optional PDF export
            pdf_data = generate_pdf(suggestions)
            st.download_button(
                label="📥 Download Suggestions as PDF",
                data=pdf_data,
                file_name="resumatch_suggestions.pdf",
                mime="application/pdf"
            )

        with st.spinner("🔎 Checking for Missing Keywords..."):
            missing = find_missing_keywords(resume_text, jd_text, top_n=10)
            st.subheader("📌 Missing Keywords from JD")
            if missing:
                st.markdown(", ".join(missing))
            else:
                st.success("✅ Your resume includes all top keywords from the JD!")
