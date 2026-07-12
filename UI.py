
from Agents.teacher_agent import teacher_agent
import streamlit as st

st.header("AI Placement Preparation Multi-Agent System")

goal = st.text_input("Goal")

mode = st.selectbox(
    "Mode",
    [
        "Learning",
        "Interview",
        "Notes",
        "Compare",
        "Coding"
    ]
)

level = st.selectbox(
    "Level",
    [
        "Beginner",
        "Intermediate",
        "Advanced"
    ]
)

language = st.selectbox(
    "language",
    [
        "english",
        "hindi",
        "hinglish"
    ]
)

query = st.text_area("Query")


if st.button("Submit"):

    response = teacher_agent(
        goal=goal,
        mode=mode,
        level=level,
        language=language,
        query=query
    )

    st.write(response)
    