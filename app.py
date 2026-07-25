#to run = python -m streamlit run app.py
import streamlit as st
from UI.Teacher_UI import teacher_page
from UI.Quiz_UI import quiz_page
from UI.Youtube_UI import youtube_page
st.set_page_config(
        page_title="🤖 AI Learning Assistant",
        page_icon="🧑‍💻",
        layout="wide"
    )

page = st.sidebar.selectbox(
    "Choose Agent",
    ["Teacher", "Quiz","YouTube_chatbot"]
)

if page == "Teacher":
    teacher_page()

elif page == "Quiz":
    quiz_page()

elif page == "YouTube_chatbot":
    youtube_page()