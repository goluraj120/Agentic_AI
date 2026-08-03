#to run = python -m streamlit run app.py
import streamlit as st
from UI.Teacher_UI import teacher_page
from UI.Quiz_UI import quiz_page
from UI.Youtube_UI import youtube_page
from UI.planner_UI import planner_page
st.set_page_config(
        page_title="🤖 AI Learning Assistant",
        page_icon="🧑‍💻",
        layout="wide"
    )

agent = st.sidebar.selectbox(
    "Select Agent",
    [
        "Teacher",
        "Quiz",
        "Planner",
        "YouTube Chatbot"
    ]
)
if agent == "Teacher":
    teacher_page()

elif agent == "Quiz":
    quiz_page()

elif agent == "Planner":
    planner_page()

elif agent == "YouTube Chatbot":
    youtube_page()