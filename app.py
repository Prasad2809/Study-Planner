import streamlit as st
from chatbot import chatbot_page
from study_planner import planner_page
from resources import resources_page
from quiz import quiz_page
from productivity import productivity_page

# ---- PAGE CONFIG ----
st.set_page_config(page_title="SmartLearn AI", layout="wide")

# ---- SESSION STATE INIT ----
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""
if "users_db" not in st.session_state:
    # Default users database
    st.session_state.users_db = {
        "test@example.com": {"password": "1234", "name": "Test User"}
    }
if "show_signup" not in st.session_state:
    st.session_state.show_signup = False

# ---- LOGIN FUNCTION ----
def login():
    st.title("🔐 Login to SmartLearn AI")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if email in st.session_state.users_db and st.session_state.users_db[email]["password"] == password:
            st.session_state.logged_in = True
            st.session_state.username = st.session_state.users_db[email]["name"]
            st.success(f"Welcome back, {st.session_state.users_db[email]['name']}! 🎉")
            st.rerun()
        else:
            st.error("Invalid email or password.")

# ---- SIGN-UP FUNCTION ----
def signup():
    st.title("📝 Create an Account")
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Sign Up"):
        if email in st.session_state.users_db:
            st.error("An account with this email already exists.")
        elif not email or not password or not name:
            st.error("Please fill all fields.")
        else:
            st.session_state.users_db[email] = {"password": password, "name": name}
            st.success("Account created successfully! Please log in.")
            st.session_state.show_signup = False

# ---- LOGIN PAGE LOGIC ----
if not st.session_state.logged_in:
    if st.session_state.show_signup:
        signup()
        if st.button("Already have an account? Login"):
            st.session_state.show_signup = False
    else:
        login()
        if st.button("Don't have an account? Sign Up"):
            st.session_state.show_signup = True
    st.stop()  # Stop execution until logged in

# ---- MAIN APP ----
st.sidebar.title("📘 SmartLearn AI")
st.sidebar.write(f"👋 Logged in as: **{st.session_state.username}**")
if st.sidebar.button("Logout"):
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.rerun()

page = st.sidebar.radio(
    "Go to",
    ["Home", "AI Tutor Chatbot", "Study Planner", "Resource Hub", "Quiz Zone", "Productivity Tracker"]
)

if page == "Home":
    st.title("📘 Welcome to SmartLearn AI")
    st.subheader("Your Personalized Tutor, Anywhere, Anytime.")
    st.write("Use the sidebar to explore features. Built with ❤️ using Streamlit + OpenAI.")
    st.success("🎯 Designed for all students – no matter your stream!")

elif page == "AI Tutor Chatbot":
    chatbot_page()

elif page == "Study Planner":
    planner_page()

elif page == "Resource Hub":
    resources_page()

elif page == "Quiz Zone":
    quiz_page()

elif page == "Productivity Tracker":
    productivity_page()
