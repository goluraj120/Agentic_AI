from Prompt.prompt_router import PROMPTS
from llms.gemini import llm
from langchain_core.output_parsers import PydanticOutputParser
from Schema.planner_schema import StudyPlan

# Create the parser
parser = PydanticOutputParser(pydantic_object=StudyPlan)


def planner_agent(goal, level, study_hours, duration, language):
    """
    Generates a personalized study plan.

    Args:
        goal (str): User's learning goal.
        level (str): Current skill level.
        study_hours (str): Available study hours per day.
        duration (str): Study duration in weeks.
        language (str): Preferred language.

    Returns:
        StudyPlan: Structured study plan.
    """

    # Fetch planner prompt
    prompt = PROMPTS.get("planner")

    if prompt is None:
        raise ValueError("Unsupported mode: planner")

    # Build the chain
    chain = prompt | llm | parser

    # Invoke the chain
    response = chain.invoke(
        {
            "goal": goal,
            "level": level,
            "study_hours": study_hours,
            "duration": duration,
            "language": language,
            "format_instructions": parser.get_format_instructions(),
        }
    )

    return response