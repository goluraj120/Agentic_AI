from Agents.teacher_agent import teacher_agent

response = teacher_agent(
    goal=input("Goal: "),
    mode=input("Mode (learning/notes/interview/compare/coding): "),
    level=input("Level: "),
    language=input("Language: "),
    query=input("Question: ")
)

print(response)
