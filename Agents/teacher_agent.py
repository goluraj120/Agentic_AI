from Prompt.prompt_router import PROMPTS
from llms.gemini import llm
from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()

def teacher_agent(goal, mode, level, language, query):

    prompt = PROMPTS.get(mode.lower())

    if prompt is None:
        raise ValueError(f"Unsupported mode: {mode}")

    chain = prompt | llm | parser

    return chain.invoke({
        "goal": goal,
        "level": level,
        "language": language,
        "query": query
    })
