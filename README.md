# ResuMatch.ai 🔍✨ 
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://resumatch-4ww7z4d7cyvfxghlpcjpfw.streamlit.app)
![Made with Python](https://img.shields.io/badge/Made%20with-Python-3776AB?logo=python&logoColor=white)
![Built with Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-ff4b4b?logo=streamlit&logoColor=white)
![Status](https://img.shields.io/badge/Status-Deployed-brightgreen)
![License](https://img.shields.io/badge/License-MIT-blue.svg)


**AI-powered Resume–Job Description Alignment Assistant**  
Analyze your resume's alignment with a job description and get AI-generated bullet point improvements all in one click.

🚀 [Live App](https://resumatch-4ww7z4d7cyvfxghlpcjpfw.streamlit.app)

---

## 💡 Features

- 📄 Upload a Resume + Job Description (PDF)
- 🤖 Instant Resume–JD Match Score (via FAISS)
- ✍️ GPT-powered Bullet Point Suggestions (mocked)
- 🧠 Keyword Gap Detection using KeyBERT
- 🖼️ Clean UI with Streamlit
- 📤 Optional export of revised bullets as PDF

---

## 🛠️ Built With

- `Streamlit` — UI Framework
- `PyMuPDF` + `pdfplumber` — PDF Text Extraction
- `FAISS` — Vector similarity search
- `KeyBERT` — Keyword extraction
- `dotenv` — Secure API key management
- `OpenAI` (mocked GPT calls for dev/testing)

---

## 🔧 Setup Locally

```bash
git clone https://github.com/sunidhijain13/resumatch.git
cd resumatch
pip install -r requirements.txt
streamlit run app.py
```

Make sure to add your OpenAI key to `.env` like:

```env
OPENAI_API_KEY=your-key-here
```

---

## 📦 Folder Structure

```text
📁 resumatch/
├── app.py
├── resume_parser.py
├── jd_parser.py
├── similarity_engine.py
├── gpt_rewriter.py
├── keyword_matcher.py
├── pdf_utils.py
├── requirements.txt
├── .gitignore
└── .env  # (excluded from repo)
```

---

## 👩‍💻 Made by

Sunidhi Jain — [LinkedIn](https://www.linkedin.com/in/sunidhijain13) 🧠✨  
MSCS @ Syracuse · AI Engineer · SU WiSE 

