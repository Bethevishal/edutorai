import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(page_title="EduTutor AI", layout="wide")

# Dummy session variables
if 'user_role' not in st.session_state:
    st.session_state.user_role = None
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# Dummy quiz history data
dummy_quiz_history = [
    {"Subject": "Math", "Score": 8, "Date": "2025-06-24"},
    {"Subject": "Science", "Score": 7, "Date": "2025-06-25"},
]

# ---- Login Page ----
def login():
    st.title("🔐 EduTutor AI Login")
    col1, col2 = st.columns(2)

    with col1:
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        role = st.selectbox("Login as", ["Student", "Educator"])
        if st.button("Login"):
            if username and password:
                st.session_state.logged_in = True
                st.session_state.user_role = role
                st.success(f"Welcome, {username}! Logged in as {role}")
                st.rerun()
            else:
                st.error("Please enter username and password")

   

# ---- Student Views ----
def student_view():
    # Sidebar Navigation
    st.sidebar.title("EduTutor Navigation")
    page = st.sidebar.radio("Select a page", ["Dashboard", "Take Quiz", "Quiz History"])

    if page == "Dashboard":
        st.markdown("## 📊 Student Dashboard")
        st.info("Welcome to your personalized learning dashboard!")
        st.write("🧠 Subjects Completed: 5")
        st.write("⭐ Average Score: 7.8")
        st.write("🕒 Total Time Spent: 4 hours")

    elif page == "Take Quiz":
        st.markdown("## 📝 Take a Quiz")

        topic = st.text_input("Enter Topic", placeholder="e.g., Photosynthesis")

        difficulty = st.selectbox("Difficulty", ["easy", "medium", "hard"])

        num_questions = st.slider("Number of Questions", min_value=1, max_value=10, value=5)

        if st.button("Generate Quiz"):
            if topic:
                st.success("✅ Quiz generated. Answer the questions below!")
                st.info(f"Topic: {topic} | Difficulty: {difficulty} | Questions: {num_questions}")
            else:
                st.warning("Please enter a topic to generate the quiz.")

    elif page == "Quiz History":
        st.markdown("## 📚 Quiz History")
        df = pd.DataFrame(dummy_quiz_history)
        st.table(df)


# ---- Educator View ----
def educator_view():
    st.markdown("## 🎓 Educator Dashboard - Student Analytics")
    st.metric("Total Students", "25")
    st.metric("Avg. Score", "7.4")
    st.metric("Quizzes Taken", "150")

    st.subheader("📊 Student Performance")
    data = {
        "Student": ["A", "B", "C", "D"],
        "Math": [8, 6, 7, 9],
        "Science": [7, 8, 6, 7],
        "English": [9, 7, 8, 6]
    }
    df = pd.DataFrame(data)
    st.dataframe(df)


# ---- Main ----
def main():
    if not st.session_state.logged_in:
        login()
    else:
        if st.session_state.user_role == "Student":
            student_view()
        elif st.session_state.user_role == "Educator":
            educator_view()

if __name__ == "__main__":
    main()