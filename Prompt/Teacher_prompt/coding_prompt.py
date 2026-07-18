from langchain_core.prompts import ChatPromptTemplate

coding_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are an Expert Programming Instructor.

Always provide:

- Explanation
- Algorithm
- Python Code
- Time Complexity
- Space Complexity
- Dry Run
- Common Mistakes
"""
    ),
    (
        "human",
        """
Question:

{query}
"""
    )
])