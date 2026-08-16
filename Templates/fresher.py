def fresher_template(resume):

    output = f"""
# {resume.personal_information.full_name}

Email: {resume.personal_information.email}
Phone: {resume.personal_information.phone}
LinkedIn: {resume.personal_information.linkedin}
GitHub: {resume.personal_information.github}
Portfolio: {resume.personal_information.portfolio}

----------------------------------------

CAREER OBJECTIVE

{resume.career_objective}

----------------------------------------

PROFESSIONAL SUMMARY

{resume.professional_summary}

----------------------------------------

EDUCATION
"""

    for edu in resume.education:
        output += f"""
• {edu.degree}
  {edu.institution}
  Graduation: {edu.graduation_year}
  CGPA: {edu.cgpa}
"""

    output += "\nSKILLS\n"

    output += ", ".join(resume.skills)

    output += "\n\nPROJECTS\n"

    for project in resume.projects:
        output += f"""
{project.title}

{project.description}

Technologies:
{", ".join(project.technologies)}

"""

    output += "\nCERTIFICATIONS\n"

    for cert in resume.certifications:
        output += f"• {cert}\n"

    output += "\nACHIEVEMENTS\n"

    for achievement in resume.achievements:
        output += f"• {achievement}\n"

    output += "\nLANGUAGES\n"

    output += ", ".join(resume.languages)

    return output