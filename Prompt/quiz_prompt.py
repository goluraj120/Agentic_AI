from langchain_core.prompts import ChatPromptTemplate

quiz_prompt = ChatPromptTemplate.from_template("""
You are an expert AI Quiz Generator.

Generate a quiz.

Goal:
{goal}

Topic:
{query}

Difficulty:
{level}

Language:
{language}

Instructions:

- Generate exactly 10 MCQs.
- Each question must have four options.
- Only one correct answer.
- Give a short explanation.
- Match the student's difficulty level.
- Return the response according to the provided schema.
""")