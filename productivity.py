import streamlit as st
import time

def productivity_page():
    st.header("⏱️ Productivity Tracker")
    st.write("Use the timer below to start a Pomodoro session (25 minutes work, 5 minutes break).")

    work_minutes = 25
    break_minutes = 5

    if st.button("Start Pomodoro"):
        # Work Session
        st.subheader("Work Session")
        with st.empty():
            for remaining in range(work_minutes * 60, 0, -1):
                mins, secs = divmod(remaining, 60)
                st.metric(label="Time Left", value=f"{mins:02d}:{secs:02d}")
                time.sleep(1)
        st.success("✅ Work session complete! Time for a 5-minute break.")

        # Break Session
        st.subheader("Break Time")
        with st.empty():
            for remaining in range(break_minutes * 60, 0, -1):
                mins, secs = divmod(remaining, 60)
                st.metric(label="Break Time Left", value=f"{mins:02d}:{secs:02d}")
                time.sleep(1)
        st.balloons()

        st.success("🎉 Break over! Ready for another Pomodoro?")