
    
import streamlit as st

def teacher_page():
    st.title("Teacher Agent")

    from Agents.teacher_agent import teacher_agent

   

    st.title("📘 Teacher Agent")

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
        ["Beginner", "Intermediate", "Advanced"]
    )

    language = st.selectbox(
        "Language",
        ["English", "Hindi", "Hinglish"]
    )

    query = st.text_area("Query")

    if st.button("Generate"):

        response = teacher_agent(
            goal,
            mode,
            level,
            language,
            query
        )

        st.markdown(response)