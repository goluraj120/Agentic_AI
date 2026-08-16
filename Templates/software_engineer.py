def software_engineer_template(resume):

    output = f"""
# {resume.personal_information.full_name}

SOFTWARE ENGINEER

----------------------------------------

SUMMARY

{resume.professional_summary}

----------------------------------------

SKILLS

"""

    output += ", ".join(resume.skills)

    output += "\n\nPROJECTS\n"

    for project in resume.projects:

        output += f"""
{project.title}

{project.description}

"""

    output += "\nEXPERIENCE\n"

    for exp in resume.experience:

        output += f"""
{exp.job_title}

{exp.company}

{exp.duration}

{exp.description}

"""

    return output
