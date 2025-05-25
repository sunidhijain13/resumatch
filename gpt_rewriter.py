def suggest_resume_bullets(resume_text: str, jd_text: str, use_mock: bool = True) -> str:
    """
    Returns optimized bullet point suggestions.
    If use_mock=True, generates fake GPT-like content.
    """
    if use_mock:
        return f"""
- Optimized resume language to match key responsibilities in the JD (mocked).
- Reframed skills and achievements to improve ATS alignment by 45% (mocked).
"""
    
    # 🛑 Real OpenAI call (disabled if no API quota)
    from openai import OpenAI
    from dotenv import load_dotenv
    import os

    load_dotenv()
    client = OpenAI()

    prompt = f"""
You're an AI resume assistant. Given the resume and job description below, suggest 2 improved bullet points that align better with the job.

Resume:
{resume_text}

Job Description:
{jd_text}

Respond with just the 2 bullet points in markdown list format.
"""

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert AI resume coach."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=300
    )

    return response.choices[0].message.content.strip()
