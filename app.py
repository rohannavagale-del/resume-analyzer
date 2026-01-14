import streamlit as st
from skills import JOB_SKILLS
from utils import extract_text_from_pdf, analyze_skills

st.set_page_config(page_title="AI Resume Analyzer", layout="centered")

st.title("📄 AI Resume Analyzer & Skill Gap Finder")
st.write("Upload your resume and check how well it matches your target job role.")

job_role = st.selectbox(
    "Select Target Job Role",
    list(JOB_SKILLS.keys())
)

uploaded_file = st.file_uploader(
    "Upload Resume (PDF only)",
    type=["pdf"]
)

if uploaded_file:
    resume_text = extract_text_from_pdf(uploaded_file)
    required_skills = JOB_SKILLS[job_role]

    matched, missing, score = analyze_skills(resume_text, required_skills)

    st.subheader("📊 Resume Match Score")
    st.progress(score / 100)
    st.write(f"**Match Percentage:** {score}%")

    st.subheader("✅ Matched Skills")
    if matched:
        st.success(", ".join(matched))
    else:
        st.warning("No matching skills found")

    st.subheader("❌ Missing Skills")
    if missing:
        st.error(", ".join(missing))
    else:
        st.success("No missing skills 🎉")

    st.subheader("🚀 Improvement Tip")
    st.info("Focus on learning missing skills to improve your resume score.")
