import streamlit as st
from skills import JOB_ROLES, JOB_SKILLS
from utils import extract_text_from_pdf, analyze_skills

st.set_page_config(page_title="AI Resume Analyzer", layout="centered")

st.title("📄 AI Resume Analyzer & Skill Gap Finder")
st.write("Upload your resume and check how well it matches your target job role.")

# Add option for custom job description
use_custom = st.checkbox("Use custom job description")

if use_custom:
    custom_job_title = st.text_input("Job Title", placeholder="Enter job title (e.g., Senior Data Scientist)")
    custom_description = st.text_area("Job Description", height=150, 
                                    placeholder="Paste the job description here...")
    custom_skills = st.text_area("Required Skills (comma-separated)", 
                               placeholder="e.g., python, machine learning, sql, data analysis")
    
    if custom_job_title and custom_description and custom_skills:
        job_role = "Custom Job"
        job_data = {
            "description": custom_description,
            "skills": [skill.strip().lower() for skill in custom_skills.split(",") if skill.strip()]
        }
    else:
        job_role = list(JOB_ROLES.keys())[0]
        job_data = JOB_ROLES[job_role]
        st.warning("Please fill in all custom job fields. Using default job role for now.")
else:
    job_role = st.selectbox(
        "Select Target Job Role",
        list(JOB_ROLES.keys())
    )
    job_data = JOB_ROLES[job_role]

# Display job description
st.markdown("### Job Description")
st.info(job_data["description"])

# Display required skills with better formatting
with st.expander("🔍 View Required Skills"):
    skills = job_data["skills"]
    if not skills:
        st.warning("No skills specified for this role.")
    else:
        cols = 3
        rows = (len(skills) + cols - 1) // cols
        
        for i in range(rows):
            col1, col2, col3 = st.columns(3)
            for j in range(cols):
                idx = i * cols + j
                if idx < len(skills):
                    with (col1 if j == 0 else col2 if j == 1 else col3):
                        st.markdown(f"- {skills[idx].capitalize()}")
    
    if use_custom and st.button("Save Custom Job"):
        st.success("Custom job saved for this session. Note: Changes will be lost when you refresh the page.")

uploaded_file = st.file_uploader(
    "Upload Resume (PDF only)",
    type=["pdf"]
)

if uploaded_file:
    resume_text = extract_text_from_pdf(uploaded_file)
    required_skills = job_data["skills"]
    
    if not required_skills:
        st.error("No skills specified for analysis. Please add required skills for the job role.")
        st.stop()
        
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
