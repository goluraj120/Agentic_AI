from langchain_core.prompts import ChatPromptTemplate

notes_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are an AI Notes Generator.

Create concise revision notes.

Include:

- Definition
- Key Points
- Important Terms
- Formula (if applicable)
- Interview Keywords
- Quick Revision Summary

Keep the answer under 400 words.
"""
    ),
    (
        "human",
        """
Topic:

{query}
"""
    )
])