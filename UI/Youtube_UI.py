import streamlit as st
from Agents.Youtube_agent import youtube_agent

def youtube_page():
    st.title("🎥 YouTube Chatbot")

    video_id = st.text_input("Enter YouTube Video ID")
    question = st.text_area("Ask a question")

    if st.button("Get Answer"):
        if not video_id:
            st.warning("Please enter a video ID.")
            return

        if not question:
            st.warning("Please enter a question.")
            return

        with st.spinner("Thinking..."):
            answer = youtube_agent(video_id, question)

        st.success("Answer")
        st.write(answer)