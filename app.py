#to run = python -m streamlit run app.py
import streamlit as st
from UI.Teacher_UI import teacher_page
from UI.Quiz_UI import quiz_page
from UI.Youtube_UI import youtube_page
from UI.planner_UI import planner_page
from UI.resume_UI import  resume_ui
st.set_page_config(
        page_title="🤖 AI Learning Assistant",
        page_icon="🧑‍💻",
        layout="wide"
    )




st.sidebar.title("Select Agent")

if "agent" not in st.session_state:
    st.session_state.agent = "Teacher"

if st.sidebar.button("Teacher", use_container_width=True):
    st.session_state.agent = "Teacher"

if st.sidebar.button("Quiz", use_container_width=True):
    st.session_state.agent = "Quiz"

if st.sidebar.button("Planner", use_container_width=True):
    st.session_state.agent = "Planner"

if st.sidebar.button("Resume Builder", use_container_width=True):
    st.session_state.agent = "Resume Builder"

if st.sidebar.button("YouTube Chatbot", use_container_width=True):
    st.session_state.agent = "YouTube Chatbot"

agent = st.session_state.agent



if agent == "Teacher":
    teacher_page()

elif agent == "Quiz":
    quiz_page()

elif agent == "Planner":
    planner_page()

elif agent == "YouTube Chatbot":
    youtube_page()

elif agent == "Resume Builder":
    resume_ui()