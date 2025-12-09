import streamlit as st
import random


users = {}

# mocck metrics generator
def generate_metrics():
    return {
        "Productivity Score": random.randint(50, 100),
        "Compliance Rating": random.randint(80, 100),
        "Happiness Index": random.randint(40, 90),
        "Loyalty Quotient": random.randint(70, 100)
    }

# Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'username' not in st.session_state:
    st.session_state.username = None
if 'metrics' not in st.session_state:
    st.session_state.metrics = None

# Main app
st.title("CITIZEN WELLNESS PORTAL™")

if not st.session_state.logged_in:
    # Login/Register Tabs
    tab1, tab2 = st.tabs(["Login", "Register"])
    
    with tab1:
        st.header("Authentication Portal")
        username = st.text_input("Username", key="login_username")
        password = st.text_input("Password", type="password", key="login_password")
        if st.button("Submit to The Algorithm"):
            if username in users and users[username] == password:
                st.session_state.logged_in = True
                st.session_state.username = username
                st.session_state.metrics = generate_metrics()
                st.success("Welcome, Citizen! Accessing your metrics...")
                st.rerun()  # Force rerun to show dashboard
            else:
                st.error("Invalid credentials. The Algorithm does not recognize you.")
    
    with tab2:
        st.header("Registration System")
        new_username = st.text_input("Username", key="reg_username")
        new_password = st.text_input("Password (min 4 chars)", type="password", key="reg_password")
        if st.button("Register with The Algorithm"):
            if not new_username:
                st.error("Username cannot be empty.")
            elif new_username in users:
                st.error("Username already taken. Choose another.")
            elif len(new_password) < 4:
                st.error("Password must be at least 4 characters.")
            else:
                users[new_username] = new_password
                st.success("Registration successful! You may now log in.")
else:
    # Dashboard
    st.header(f"Welcome, Citizen {st.session_state.username}!")
    st.subheader("YOUR ALGORITHMIC SATISFACTION METRICS™")
    
    metrics = st.session_state.metrics
    for metric, value in metrics.items():
        st.write(f"{metric}: {'█' * (value // 10)}{'░' * (10 - value // 10)} {value}%")
    
    # Status based on average
    avg = sum(metrics.values()) / len(metrics)
    if avg >= 80:
        status = "WITHIN ACCEPTABLE PARAMETERS"
    elif avg >= 60:
        status = "REQUIRES OPTIMIZATION"
    else:
        status = "CRITICAL ATTENTION NEEDED"
    st.write(f"Status: {status}")
    
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = None
        st.session_state.metrics = None
        st.success("Logged out. The Algorithm awaits your return.")
        st.rerun()