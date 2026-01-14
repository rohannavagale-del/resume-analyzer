import streamlit as st
from skills import JOB_SKILLS, JOB_DESCRIPTIONS
from utils import extract_text_from_pdf, analyze_skills
from learning_resources import LEARNING_RESOURCES

st.set_page_config(page_title="AI Resume Analyzer", layout="centered")

st.title("📄 AI Resume Analyzer & Skill Gap Finder")
st.write("Upload your resume and check how well it matches your target job role.")

job_role = st.selectbox(
    "Select Target Job Role",
    list(JOB_SKILLS.keys())
)

# Display job description
if job_role in JOB_DESCRIPTIONS:
    st.info(f"**{job_role}**: {JOB_DESCRIPTIONS[job_role]}")

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
        
        # Display learning resources for missing skills
        st.subheader("📚 Learning Resources")
        st.info("Here are some resources to help you learn the missing skills:")
        
        for skill in missing:
            skill_lower = skill.lower()
            resources = LEARNING_RESOURCES.get(skill_lower, LEARNING_RESOURCES['default'])
            
            # If using default, modify the search URL
            if resources == LEARNING_RESOURCES['default']:
                search_query = skill.replace(' ', '+')
                for resource in resources:
                    st.markdown(f"- [{resource['title']}]({resource['url']}{search_query}) ({resource['platform']})")
            else:
                for resource in resources:
                    st.markdown(f"- [{resource['title']}]({resource['url']}) ({resource['platform']})")
            
    else:
        st.success("No missing skills 🎉")

    st.subheader("🚀 Improvement Tip")
    st.info("Check out the learning resources above to improve your skills and increase your resume match score!")
