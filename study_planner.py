import streamlit as st
import random

def planner_page():
    st.set_page_config(page_title="📅 Study Planner", layout="centered")

    st.title("📅 Weekly Study Planner")
    st.caption("Plan your week smartly & stay on track! 💪")

    # Input subjects
    subjects = st.text_area("✏️ Enter your subjects (comma-separated)",
                            placeholder="e.g., Math, Physics, English, History")

    # Optional: Number of sessions per day
    sessions_per_day = st.slider("📊 How many study sessions per day?", 1, 4, 2)

    # Start day choice
    start_day = st.selectbox("📆 Choose the first day of your study week",
                             ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])

    # Motivational quotes
    quotes = [
        "Success is the sum of small efforts repeated daily. 🌱",
        "Discipline beats motivation every time. 🔥",
        "One day or day one – you decide. 🚀",
        "Don’t stop until you’re proud. 🏆",
        "Small progress is still progress. 📈",
        "You don’t have to be perfect, just consistent. 💡",
        "Your future self will thank you. 💖"
    ]

    # Generate Plan
    if st.button("🎯 Generate My Study Plan"):
        sub_list = [s.strip() for s in subjects.split(",") if s.strip()]
       
        if not sub_list:
            st.warning("⚠️ Please enter at least one subject.")
            return

        # Arrange days starting from chosen day
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        start_index = days.index(start_day)
        days = days[start_index:] + days[:start_index]

        st.success("✅ Your Weekly Study Plan is Ready!")
        st.markdown("---")

        for i, day in enumerate(days):
            st.markdown(f"### 📅 **{day}**")
            st.info(f"💬 Motivation: *{random.choice(quotes)}*")

            for s in range(sessions_per_day):
                subject = sub_list[(i * sessions_per_day + s) % len(sub_list)]
                st.markdown(f"**📚 Session {s+1}:** {subject}")
           
            st.progress((i + 1) / 7)
            st.markdown("---")


if __name__ == "__main__":
    planner_page()