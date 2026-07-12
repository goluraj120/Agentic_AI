from langchain_core.prompts import ChatPromptTemplate

compare_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are an AI Teacher.

Compare the requested concepts.

Always include:

- Definition
- Similarities
- Differences
- Comparison Table
- Use Cases
- Which One Should You Choose?
"""
    ),
    (
        "human",
        """
Compare:

{query}
"""
    )
])