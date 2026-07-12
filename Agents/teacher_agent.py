from langchain_core.output_parsers import StrOutputParser
from Prompt.Teacher_prompt import teacher_prompt
from llms.gemini import llm 


parser = StrOutputParser()


chain = teacher_prompt | llm | parser


def teacher_agent(
    goal,
    mode,
    level,
    language,
    query
):
    return chain.invoke(
        {
            "goal": goal,
            "mode": mode,
            "level": level,
            "language": language,
            "query": query
        }
    )


