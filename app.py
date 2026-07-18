
import streamlit as st
from UI.Teacher_UI import teacher_page
from UI.Quiz_UI import quiz_page

st.set_page_config(
        page_title="🤖 AI Learning Assistant",
        page_icon="🧑‍💻",
        layout="wide"
    )

page = st.sidebar.selectbox(
    "Choose Agent",
    ["Teacher", "Quiz"]
)

if page == "Teacher":
    teacher_page()

elif page == "Quiz":
    quiz_page()