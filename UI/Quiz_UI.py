import streamlit as st
from Agents.quiz_agent import quiz_agent


def quiz_page():

    st.title("📝 AI Quiz Generator")
    st.write("Generate quizzes based on any topic.")

    # -----------------------------
    # User Inputs
    # -----------------------------

    goal = st.text_input(
        "Learning Goal",
        placeholder="Example: Learn Python"
    )

    query = st.text_input(
        "Topic",
        placeholder="Example: Functions"
    )

    level = st.selectbox(
        "Difficulty Level",
        [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    )

    language = st.selectbox(
        "Language",
        [
            "English",
            "Hindi"
        ]
    )

    # -----------------------------
    # Generate Quiz
    # -----------------------------

    if st.button("Generate Quiz"):

        if not goal or not query:
            st.warning("Please fill all fields.")
            st.stop()

        with st.spinner("Generating Quiz..."):

            try:

                quiz = quiz_agent(
                    goal=goal,
                    level=level,
                    language=language,
                    query=query
                )

                st.session_state.quiz = quiz
                st.session_state.answers = {}

            except Exception as e:

                st.error("Failed to generate quiz.")
                st.exception(e)
                st.stop()

    # -----------------------------
    # Display Quiz
    # -----------------------------

    if "quiz" not in st.session_state:
        return

    quiz = st.session_state.quiz

    st.divider()

    st.header(quiz.title)

    st.write(f"**Topic:** {quiz.topic}")
    st.write(f"**Level:** {quiz.level}")
    st.write(f"**Language:** {quiz.language}")
    st.write(f"**Questions:** {quiz.total_questions}")

    st.divider()

    # -----------------------------
    # Questions
    # -----------------------------

    for q in quiz.questions:

        st.subheader(f"Q{q.id}. {q.question}")

        answer = st.radio(

            "Choose your answer",

            options=list(q.options.keys()),

            format_func=lambda x: f"{x}. {q.options[x]}",

            key=f"q_{q.id}"

        )

        st.session_state.answers[q.id] = answer

        st.divider()

    # -----------------------------
    # Submit
    # -----------------------------

    if st.button("Submit Quiz"):

        score = 0

        st.header("📊 Result")

        for q in quiz.questions:

            user_answer = st.session_state.answers[q.id]

            if user_answer == q.answer:

                score += q.marks

                st.success(f"Question {q.id}: Correct ✅")

            else:

                st.error(f"Question {q.id}: Incorrect ❌")

                st.write(
                    f"**Correct Answer:** {q.answer} - {q.options[q.answer]}"
                )

            st.info(q.explanation)

            st.divider()

        st.success(
            f"🎉 Final Score: {score}/{quiz.total_marks}"
        )