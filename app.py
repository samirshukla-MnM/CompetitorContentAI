import streamlit as st

st.set_page_config(
    page_title="Competitor Content Intelligence",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# Sidebar
# -----------------------------

st.sidebar.title("🧠 CCI")

menu = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Upload Excel",
        "URL Manager",
        "Run Scan",
        "History",
        "Settings"
    ]
)

# -----------------------------
# Dashboard
# -----------------------------

if menu == "Dashboard":

    st.title("Competitor Content Intelligence")

    st.write(
        "Monitor competitor report pages and receive AI-powered change alerts."
    )

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Reports", "0")
    c2.metric("Competitors", "0")
    c3.metric("Today's Changes", "0")
    c4.metric("Critical Alerts", "0")

    st.divider()

    st.subheader("System Status")

    st.success("Application initialized successfully.")

    st.info("Upload an Excel file to begin monitoring.")

elif menu == "Upload Excel":

    st.title("Upload Excel")

    uploaded_file = st.file_uploader(
        "Choose Excel File",
        type=["xlsx"]
    )

    if uploaded_file:
        st.success("Excel uploaded successfully.")

elif menu == "URL Manager":

    st.title("URL Manager")

    st.info("No reports added yet.")

elif menu == "Run Scan":

    st.title("Run Scan")

    if st.button("Start Monitoring"):

        st.warning("Crawler will be implemented in Milestone 3.")

elif menu == "History":

    st.title("History")

    st.info("No scan history available.")

elif menu == "Settings":

    st.title("Settings")

    st.text_input("Sender Email")

    st.text_input("Receiver Email")

    st.selectbox(
        "Schedule",
        [
            "Daily",
            "Weekly",
            "Monthly"
        ]
    )
