import PyPDF2

def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""

    for page in reader.pages:
        text += page.extract_text()

    return text.lower()


def analyze_skills(resume_text, required_skills):
    matched = []
    missing = []

    for skill in required_skills:
        if skill in resume_text:
            matched.append(skill)
        else:
            missing.append(skill)

    match_percentage = int((len(matched) / len(required_skills)) * 100)

    return matched, missing, match_percentage
