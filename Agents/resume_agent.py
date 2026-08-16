from langchain_core.output_parsers import PydanticOutputParser
from llms.gemini import llm

from Prompt.resume_prompt import resume_prompt
from Schema.resume_schema import Resume


# ---------------------------------------------
# Output Parser
# ---------------------------------------------

parser = PydanticOutputParser(
    pydantic_object=Resume
)


# ---------------------------------------------
# Resume Generation Chain
# ---------------------------------------------

resume_chain = (
    resume_prompt.partial(
        format_instructions=parser.get_format_instructions()
    )
    | llm
    | parser
)


# ---------------------------------------------
# Resume Builder Agent
# ---------------------------------------------

def resume_agent(
    target_role,
    template,
    name,
    email,
    phone,
    linkedin,
    github,
    portfolio,
    career_objective,
    education,
    skills,
    projects,
    experience,
    certifications,
    achievements,
    languages
):
    """
    Generates an ATS-friendly resume.

    Returns:
        Resume (Pydantic Model)
    """

    response = resume_chain.invoke(
        {
            "target_role": target_role,
            "template": template,
            "name": name,
            "email": email,
            "phone": phone,
            "linkedin": linkedin,
            "github": github,
            "portfolio": portfolio,
            "career_objective": career_objective,
            "education": education,
            "skills": skills,
            "projects": projects,
            "experience": experience,
            "certifications": certifications,
            "achievements": achievements,
            "languages": languages,
        }
    )

    return response

