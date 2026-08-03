import streamlit as st

from Agents.planner_agent import planner_agent


def planner_page():
    st.title("🗓️ AI Study Planner")

    st.markdown(
        """
Generate a personalized weekly study roadmap based on your learning goal,
current level, available study time, and preferred language.
"""
    )

    # ----------------------------
    # User Inputs
    # ----------------------------

    goal = st.text_input(
        "🎯 Learning Goal",
        placeholder="Example: Become an AI Engineer"
    )

    level = st.selectbox(
        "📚 Current Level",
        [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    )

    study_hours = st.number_input(
        "⏰ Study Hours Per Day",
        min_value=1,
        max_value=12,
        value=2,
        step=1
    )

    duration = st.number_input(
        "📅 Study Duration (Weeks)",
        min_value=1,
        max_value=52,
        value=12,
        step=1
    )

    language = st.selectbox(
        "🌐 Preferred Language",
        [
            "English",
            "Hindi"
        ]
    )

    # ----------------------------
    # Generate Button
    # ----------------------------

    if st.button("🚀 Generate Study Plan"):

        if not goal.strip():
            st.warning("Please enter your learning goal.")
            return

        with st.spinner("Generating your personalized study plan..."):

            try:

                study_plan = planner_agent(
                    goal=goal,
                    level=level,
                    study_hours=study_hours,
                    duration=duration,
                    language=language,
                )

                st.success("Study Plan Generated Successfully!")

                # ----------------------------
                # Plan Details
                # ----------------------------

                st.header(study_plan.title)

                st.write(f"**Goal:** {study_plan.goal}")
                st.write(f"**Level:** {study_plan.level}")
                st.write(f"**Duration:** {study_plan.duration} Weeks")
                st.write(f"**Language:** {study_plan.language}")
                st.write(
                    f"**Estimated Total Study Hours:** {study_plan.total_study_hours}"
                )

                st.divider()

                # ----------------------------
                # Weekly Plan
                # ----------------------------

                for week in study_plan.weeks:

                    with st.expander(f"Week {week.week_number}"):

                        st.subheader("📖 Topics")

                        for topic in week.topics:
                            st.write(f"• {topic}")

                        st.subheader("🎯 Learning Objectives")

                        for objective in week.learning_objectives:
                            st.write(f"• {objective}")

                        st.subheader("⏰ Estimated Study Hours")

                        st.write(f"{week.estimated_study_hours} Hours")

                        st.subheader("🔄 Revision")

                        if week.revision:
                            st.success("Revision Week")
                        else:
                            st.info("No Revision Scheduled")

                        st.subheader("🤖 Recommended Agents")

                        for agent in week.recommended_agents:
                            st.write(f"✅ {agent}")

            except Exception as e:

                st.error(f"Error: {e}")