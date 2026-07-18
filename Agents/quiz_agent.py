from Prompt.quiz_prompt import quiz_prompt
from Schema.quiz_schema import Quiz
from llms.gemini import llm

structured_llm = llm.with_structured_output(Quiz)

chain = quiz_prompt | structured_llm


def quiz_agent(goal, level, language, query):

    return chain.invoke(
        {
            "goal": goal,
            "level": level,
            "language": language,
            "query": query,
        }
    )