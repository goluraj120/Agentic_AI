# # import Teacher_UI 

# import streamlit as st

# # -----------------------------
# # Page Configuration
# # -----------------------------
# st.set_page_config(
#     page_title="AI Learning Assistant",
#     page_icon="🤖",
#     layout="wide"
# )

# # -----------------------------
# # Sidebar
# # -----------------------------
# st.sidebar.title("🤖 AI Learning Assistant")

# page = st.sidebar.selectbox(
#     "Select Agent",
#     [
#         "Teacher Agent",
#         "Quiz Agent",
#         "Planner Agent"
#     ]
# )

# # -----------------------------
# # Load Selected Agent
# # -----------------------------
# if page == "Teacher Agent":
#     import Teacher_UI

# elif page == "Quiz Agent" :
#     import Quiz_UI

# elif page == "Planner Agent":
#     import Planner_UI

import streamlit as st
from UI.Teacher_UI import teacher_page
from UI.Quiz_UI import quiz_page

st.set_page_config(
        page_title="AI Placement Preparation Multi-Agent System",
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