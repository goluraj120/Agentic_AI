from Agents.teacher_agent import teacher_agent

response = teacher_agent(
    goal=input("Enetr your gole(like- Become AI Engineer) :"),
    mode=input("choose the mode(like- learning , interview , notes) :"),
    level=input("choose your level :"),
    language= input("choose your language(hindi , english) :"),
    query=input("Enter your query :")
)

print(response)


