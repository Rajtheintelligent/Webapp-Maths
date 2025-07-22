import streamlit as st

# --- Page Config ---
st.set_page_config(
    page_title="Grade 10 Assessment Hub",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Sidebar ---
st.sidebar.title("🔧 Select Parameters")
board = st.sidebar.selectbox("Select Board", ["SSC", "ICSE"])
subject = st.sidebar.selectbox("Select Subject", ["Mathematics", "Science", "English", "Social Studies"])

branch = None
if subject == "Mathematics":
    branch = st.sidebar.selectbox("Select Branch", ["Algebra", "Geometry"])

# Spacer to push feedback button to bottom
st.sidebar.markdown("<br><br><br><br><br><br><br><br><br><br><br>", unsafe_allow_html=True)

# --- Feedback Button (at bottom of sidebar) ---
st.sidebar.link_button("📩 Feedback Form", "https://example.com/feedback-form")

# --- Main Page ---
st.title("📘 Grade 10 – Assessment Hub")
st.markdown("Use the sidebar to choose the board, subject, and chapter. Assessments will be shown below.")

if subject == "Mathematics" and branch == "Algebra":
    chapter = st.selectbox("Select Chapter", [
        "Quadratic Equations",
        "Linear Equations in Two Variables",
        "Arithmetic Progression",
        "Probability",
        "Statistics and Financial Planning"
    ])

    if chapter == "Quadratic Equations":
        st.subheader("📂 Sub-topics in Quadratic Equations")

        subtopics = {
            "Roots of a Quadratic Equation": {
                "Form": "https://example.com/form1",
                "Kahoot": "https://example.com/kahoot1",
                "Blooket": "https://example.com/blooket1"
            },
            "Nature of Roots": {
                "Form": "https://example.com/form2",
                "Kahoot": "https://example.com/kahoot2",
                "Blooket": "https://example.com/blooket2"
            },
            "Factorisation Method": {
                "Form": "https://example.com/form3",
                "Kahoot": "https://example.com/kahoot3",
                "Blooket": "https://example.com/blooket3"
            },
            "Formative Assessment (Entire Chapter)": {
                "Form": "https://example.com/form4",
                "Kahoot": "https://example.com/kahoot4",
                "Blooket": "https://example.com/blooket4"
            }
        }

        for topic, links in subtopics.items():
            with st.expander(f"🔹 {topic}"):
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.link_button("Open Form", links["Form"])
                with col2:
                    st.link_button("Open Kahoot", links["Kahoot"])
                with col3:
                    st.link_button("Open Blooket", links["Blooket"])
    else:
        st.info("This chapter doesn’t have sub-topics added yet.")

elif subject != "Mathematics":
    st.info(f"Content for **{subject}** ({board} Board) is coming soon.")
