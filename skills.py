SKILL_RESOURCES = {
    "python": {
        "youtube": "https://www.youtube.com/watch?v=rfscVS0vtbw",
        "coursera": "https://www.coursera.org/learn/python"
    },
    "pandas": {
        "youtube": "https://www.youtube.com/watch?v=dcqPhpY7tWk",
        "coursera": "https://www.coursera.org/learn/data-analysis-with-python"
    },
    "numpy": {
        "youtube": "https://www.youtube.com/watch?v=QUT1VHiLmmI",
        "coursera": "https://www.coursera.org/learn/python-numpy"
    },
    "machine learning": {
        "youtube": "https://www.youtube.com/watch?v=NWONeJKn6kc",
        "coursera": "https://www.coursera.org/learn/machine-learning"
    },
    "statistics": {
        "youtube": "https://www.youtube.com/watch?v=xxpc-HPKN28",
        "coursera": "https://www.coursera.org/learn/statistics-for-data-science-python"
    },
    "scikit-learn": {
        "youtube": "https://www.youtube.com/watch?v=0LtBwT5uaD4",
        "coursera": "https://www.coursera.org/learn/machine-learning-with-python"
    },
    "sql": {
        "youtube": "https://www.youtube.com/watch?v=HXV3zeQKqGY",
        "coursera": "https://www.coursera.org/learn/sql-for-data-science"
    },
    "data visualization": {
        "youtube": "https://www.youtube.com/watch?v=3m7BgIvC-uQ",
        "coursera": "https://www.coursera.org/learn/python-for-data-visualization"
    },
    "html": {
        "youtube": "https://www.youtube.com/watch?v=qz0aGYrrlhU",
        "coursera": "https://www.coursera.org/learn/html"
    },
    "css": {
        "youtube": "https://www.youtube.com/watch?v=1Rs2ND1ryYc",
        "coursera": "https://www.coursera.org/learn/introcss"
    },
    "javascript": {
        "youtube": "https://www.youtube.com/watch?v=PkZNo7MFNFg",
        "coursera": "https://www.coursera.org/learn/javascript"
    },
    "react": {
        "youtube": "https://www.youtube.com/watch?v=bMknfKXIFA8",
        "coursera": "https://www.coursera.org/learn/front-end-react"
    },
    "node": {
        "youtube": "https://www.youtube.com/watch?v=Oe421EPjeBE",
        "coursera": "https://www.coursera.org/learn/server-side-nodejs"
    },
    "express": {
        "youtube": "https://www.youtube.com/watch?v=L72fhGm1tfE",
        "coursera": "https://www.coursera.org/learn/web-frameworks"
    },
    "mongodb": {
        "youtube": "https://www.youtube.com/watch?v=2QQGWYe7IDU",
        "coursera": "https://www.coursera.org/learn/mongodb"
    },
    "api": {
        "youtube": "https://www.youtube.com/watch?v=GZvSYJDk-us",
        "coursera": "https://www.coursera.org/learn/apis"
    }
}

JOB_ROLES = {
    "Data Scientist": {
        "description": "Data Scientists analyze and interpret complex data to help organizations make better decisions. They use statistical analysis, machine learning, and data visualization techniques to extract insights from data.",
        "skills": [
            "python", "pandas", "numpy", "machine learning",
            "statistics", "scikit-learn", "sql", "data visualization"
        ]
    },
    "Web Developer": {
        "description": "Web Developers design and build websites, ensuring they are visually appealing, user-friendly, and functional across different devices and browsers.",
        "skills": [
            "html", "css", "javascript", "react",
            "node", "express", "mongodb", "api"
        ]
    },
    "ML Engineer": {
        "description": "Machine Learning Engineers develop and deploy machine learning models, working on the infrastructure and systems that enable AI applications.",
        "skills": [
            "python", "machine learning", "deep learning",
            "tensorflow", "pytorch", "docker", "cloud"
        ]
    },
    "DevOps Engineer": {
        "description": "DevOps Engineers bridge the gap between development and operations, implementing CI/CD pipelines, infrastructure as code, and automation to streamline software delivery.",
        "skills": [
            "docker", "kubernetes", "aws", "azure", "gcp",
            "ci/cd", "terraform", "ansible", "linux", "python"
        ]
    },
    "Frontend Developer": {
        "description": "Frontend Developers create the visual and interactive elements of websites and web applications, focusing on user experience and interface design.",
        "skills": [
            "javascript", "react", "typescript", "html5", "css3",
            "redux", "next.js", "responsive design", "webpack", "jest"
        ]
    },
    "Backend Developer": {
        "description": "Backend Developers build and maintain the server-side of web applications, handling data storage, security, and application logic.",
        "skills": [
            "python", "java", "node.js", "django", "flask",
            "spring boot", "sql", "nosql", "rest api", "graphql"
        ]
    },
    "Data Analyst": {
        "description": "Data Analysts collect, process, and perform statistical analyses of data to help organizations make data-driven decisions.",
        "skills": [
            "sql", "excel", "tableau", "power bi", "python",
            "r", "data visualization", "statistics", "pandas", "numpy"
        ]
    },
    "Cybersecurity Analyst": {
        "description": "Cybersecurity Analysts protect computer systems and networks from cyber threats, implementing security measures and responding to security breaches.",
        "skills": [
            "security", "network security", "penetration testing", "firewall",
            "siem", "incident response", "python", "linux", "encryption"
        ]
    },
    "Cloud Architect": {
        "description": "Cloud Architects design and implement cloud computing solutions, ensuring they are secure, scalable, and meet business requirements.",
        "skills": [
            "aws", "azure", "gcp", "cloud security", "terraform",
            "kubernetes", "docker", "devops", "networking", "python"
        ]
    }
}

# For backward compatibility
JOB_SKILLS = {role: data["skills"] for role, data in JOB_ROLES.items()}
