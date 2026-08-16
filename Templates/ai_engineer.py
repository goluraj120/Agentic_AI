def ai_engineer_template(resume):

    output = f"""
# {resume.personal_information.full_name}

AI ENGINEER

Email: {resume.personal_information.email}
Phone: {resume.personal_information.phone}

LinkedIn:
{resume.personal_information.linkedin}

GitHub:
{resume.personal_information.github}

Portfolio:
{resume.personal_information.portfolio}

========================================

PROFESSIONAL SUMMARY

{resume.professional_summary}

========================================

TECHNICAL SKILLS

"""

    output += ", ".join(resume.skills)

    output += "\n\nRECOMMENDED AI SKILLS\n"

    output += ", ".join(resume.suggested_skills)

    output += "\n\nPROJECTS\n"

    for project in resume.projects:

        output += f"""
{project.title}

{project.description}

Tech Stack:
{", ".join(project.technologies)}

"""

    output += "\nEDUCATION\n"

    for edu in resume.education:

        output += f"""
{edu.degree}

{edu.institution}

{edu.graduation_year}

CGPA: {edu.cgpa}

"""

    if resume.experience:

        output += "\nEXPERIENCE\n"

        for exp in resume.experience:

            output += f"""
{exp.job_title}

{exp.company}

{exp.duration}

{exp.description}

"""

    return output