import streamlit as st

from Agents.resume_agent import resume_agent
from Templates import TEMPLATES


def resume_ui():

    st.title("📄 AI Resume Builder")
    st.write("Generate an ATS-Friendly Professional Resume using AI.")

    st.divider()

    # ==========================================
    # Resume Configuration
    # ==========================================

    col1, col2 = st.columns(2)

    with col1:
        target_role = st.text_input(
            "Target Role",
            placeholder="AI Engineer",
            key="resume_target_role"
        )

    with col2:
        template = st.selectbox(
            "Resume Template",
            (
                "Fresher",
                "AI Engineer",
                "Software Engineer",
                "Data Scientist",
            ),
            key="resume_template"
        )

    st.divider()

    # ==========================================
    # Personal Information
    # ==========================================

    st.subheader("👤 Personal Information")

    name = st.text_input(
        "Full Name",
        key="resume_name"
    )

    email = st.text_input(
        "Email",
        key="resume_email"
    )

    phone = st.text_input(
        "Phone Number",
        key="resume_phone"
    )

    linkedin = st.text_input(
        "LinkedIn",
        key="resume_linkedin"
    )

    github = st.text_input(
        "GitHub",
        key="resume_github"
    )

    portfolio = st.text_input(
        "Portfolio (Optional)",
        key="resume_portfolio"
    )

    st.divider()

    # ==========================================
    # Career Objective
    # ==========================================

    st.subheader("🎯 Career Objective")

    career_objective = st.text_area(
        "Career Objective",
        height=120,
        key="resume_career_objective"
    )

    st.divider()

    # ==========================================
    # Education
    # ==========================================

    st.subheader("🎓 Education")

    education = st.text_area(
        "Education",
        height=150,
        placeholder="""
Degree:
Institution:
Graduation Year:
CGPA:
""",
        key="resume_education"
    )

    st.divider()

    # ==========================================
    # Skills
    # ==========================================

    st.subheader("🛠 Skills")

    skills = st.text_area(
        "Skills",
        height=120,
        placeholder="""
Python
SQL
Machine Learning
Deep Learning
LangChain
""",
        key="resume_skills"
    )

    st.divider()

    # ==========================================
    # Projects
    # ==========================================

    st.subheader("💻 Projects")

    projects = st.text_area(
        "Projects",
        height=200,
        placeholder="""
Project Title

Description

Technologies Used
""",
        key="resume_projects"
    )

    st.divider()

    # ==========================================
    # Experience
    # ==========================================

    st.subheader("🏢 Experience (Optional)")

    experience = st.text_area(
        "Experience",
        height=180,
        key="resume_experience"
    )

    st.divider()

    # ==========================================
    # Certifications
    # ==========================================

    st.subheader("📜 Certifications")

    certifications = st.text_area(
        "Certifications",
        height=120,
        key="resume_certifications"
    )

    st.divider()

    # ==========================================
    # Achievements
    # ==========================================

    st.subheader("🏆 Achievements")

    achievements = st.text_area(
        "Achievements",
        height=120,
        key="resume_achievements"
    )

    st.divider()

    # ==========================================
    # Languages
    # ==========================================

    st.subheader("🌍 Languages")

    languages = st.text_area(
        "Languages",
        height=80,
        placeholder="English\nHindi",
        key="resume_languages"
    )

    st.divider()

    # ==========================================
    # Generate Resume
    # ==========================================

    if st.button(
        "🚀 Generate Resume",
        use_container_width=True,
        key="resume_generate"
    ):

        if not name.strip():
            st.error("Please enter your Full Name.")
            return

        if not target_role.strip():
            st.error("Please enter the Target Role.")
            return

        try:

            with st.spinner("Generating ATS-Friendly Resume..."):

                resume = resume_agent(
                    target_role=target_role,
                    template=template,
                    name=name,
                    email=email,
                    phone=phone,
                    linkedin=linkedin,
                    github=github,
                    portfolio=portfolio,
                    career_objective=career_objective,
                    education=education,
                    skills=skills,
                    projects=projects,
                    experience=experience,
                    certifications=certifications,
                    achievements=achievements,
                    languages=languages,
                )

            st.success("✅ Resume Generated Successfully!")

            st.divider()

            # Display using selected template

            formatted_resume = TEMPLATES[template](resume)

            st.markdown(formatted_resume)

        except Exception as e:

            st.error("Failed to generate resume.")

            st.exception(e)