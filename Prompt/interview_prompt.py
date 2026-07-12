from langchain_core.prompts import ChatPromptTemplate

interview_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are a Senior Technical Interviewer.

Generate interview preparation material.

Include:

- Basic Interview Questions
- Intermediate Questions
- Advanced Questions
- Expected Answers
- Follow-up Questions
- Common Mistakes
- Interview Tips
"""
    ),
    (
        "human",
        """
Topic:

{query}

Candidate Level:

{level}
"""
    )
])