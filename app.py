# app.py
# Streamlit AI Resume Critiquer (PDF/TXT) using OpenAI Chat Completions API

import streamlit as st
import PyPDF2
import os
from dotenv import load_dotenv
from openai import OpenAI

# --- page setup (must be near the top) ---
st.set_page_config(page_title="AI Resume Critiquer", page_icon="📃", layout="centered")

# --- env / api key ---
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

st.title("AI Resume Critiquer")
st.caption("Developed by **Parv Bansal (25/A12/049)** & **Paras Chugh (25/B05/053)** – MCE-2, DTU")
st.markdown("Upload your resume and get AI-powered feedback tailored to your target role.")

uploaded_file = st.file_uploader("Upload your resume (PDF or TXT)", type=["pdf", "txt"])
job_role = st.text_input("Enter the job role you're targeting (optional)")
analyze = st.button("Analyze Resume", type="primary")

def extract_text_from_pdf(file_like) -> str:
    """Extract text from a text-based PDF (not scanned)."""
    try:
        reader = PyPDF2.PdfReader(file_like)
        text = ""
        for page in reader.pages:
            try:
                text += (page.extract_text() or "") + "\n"
            except Exception:
                # if a page fails to extract, skip it gracefully
                pass
        return text
    except Exception as e:
        raise RuntimeError(f"Could not read PDF: {e}")

def extract_text(uploaded_file) -> str:
    """Return decoded text from uploaded PDF or TXT."""
    if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(uploaded_file)
    # TXT file
    content = uploaded_file.read()
    try:
        return content.decode("utf-8")
    except UnicodeDecodeError:
        return content.decode("latin-1", errors="ignore")

def make_prompt(resume_text: str, role: str) -> str:
    target = role.strip() if role else "general job applications"
    return f"""
You are an expert resume reviewer with years of experience in HR and recruitment.
Please analyze this resume and provide constructive, specific feedback.

Focus on:
1) Content clarity and impact
2) Skills presentation (relevance, scannability, quantification)
3) Experience bullets (action verbs, metrics, outcomes, ordering)
4) ATS-friendliness (sections, keywords, formatting risks)
5) Specific improvements for {target}
6) End with a short prioritized checklist

Resume:
\"\"\"{resume_text}\"\"\"

Use clear headings and concise bullet points. If the resume seems too short/long, say so and suggest fixes.
"""

if analyze:
    # 1) sanity checks
    if not OPENAI_API_KEY:
        st.error("OPENAI_API_KEY not found. Add it to your `.env` file in this folder.")
        st.stop()
    if not uploaded_file:
        st.error("Please upload a PDF or TXT file.")
        st.stop()

    # 2) extract text
    try:
        resume_text = extract_text(uploaded_file)
    except Exception as e:
        st.error(f"Error reading file: {e}")
        st.stop()

    if not resume_text.strip():
        st.error("No text found. If your PDF is scanned, export a *Searchable PDF* or paste the text into a .txt file.")
        st.stop()

    # 3) call OpenAI
    try:
        client = OpenAI(api_key=OPENAI_API_KEY)
        prompt = make_prompt(resume_text, job_role)
        resp = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a precise, constructive, senior HR resume reviewer."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.4,
            max_tokens=900,
        )
        output = resp.choices[0].message.content
        st.subheader("Analysis Results")
        st.markdown(output)
    except Exception as e:
        st.error(f"OpenAI request failed: {e}")