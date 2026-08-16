def data_scientist_template(resume):

    output = f"""
# {resume.personal_information.full_name}

DATA SCIENTIST

========================================

SUMMARY

{resume.professional_summary}

========================================

SKILLS

"""

    output += ", ".join(resume.skills)

    output += "\n\nPROJECTS\n"

    for project in resume.projects:

        output += f"""
{project.title}

{project.description}

"""

    output += "\nEDUCATION\n"

    for edu in resume.education:

        output += f"""
{edu.degree}

{edu.institution}

CGPA: {edu.cgpa}

"""

    return output
