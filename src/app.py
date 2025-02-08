import logging
import time
import streamlit as st
import sys
import os
from pathlib import Path

# Add the 'src' directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

# Import necessary functions from utils
from utils.logging import configure_logging
from utils.aws import fetch_aws_credentials, request_user_credentials

# Function to set a background
def set_background(image_path):
    """
    Set the background image for the Streamlit app.
    :param image_path: Path to the background image.
    """
    if Path(image_path).exists():
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("file://{os.path.abspath(image_path)}");
                background-size: cover;
                background-repeat: no-repeat;
                background-attachment: fixed;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    else:
        st.warning(f"Background image not found: {image_path}")

# Configure logging with rich formatting
configure_logging()

# Set page title and layout
st.set_page_config(
    page_title="Cloud Automation Suite",
    page_icon="🌩️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# UI Header
st.title("🌩️ Cloud Automation Suite 🚀")
st.caption("Empowering businesses with cutting-edge cloud automation solutions.")

# Set Background
set_background("assets/background.png")

# Check if session state for page choice exists, else initialize it
if 'page' not in st.session_state:
    st.session_state.page = "🏠 Home"

# Sidebar menu navigation
menu = ["🏠 Home", "📊 Dashboard", "🛠️ Terraform Automation", "👤 About", "📞 Contact"]
choice = st.sidebar.selectbox("🔍 Menu", menu, index=menu.index(st.session_state.page))

# Update session state with selected page
st.session_state.page = choice

# Add a delay before checking credentials
def delay_and_check_credentials():
    with st.spinner("Checking for AWS credentials..."):
        time.sleep(2)  # Delay for 2 seconds to simulate the check
    logging.debug("Checking for credentials completed.")

    # Try to fetch credentials from Streamlit secrets
    access_key, secret_key = fetch_aws_credentials()

    if not access_key or not secret_key:
        # If credentials are not found, prompt the user for input
        st.warning("AWS credentials not found in secrets. Please enter them manually.")
        access_key, secret_key = request_user_credentials()
        
    return access_key, secret_key

# Fetch AWS credentials
access_key, secret_key = delay_and_check_credentials()

# Display the credentials status
if access_key and secret_key:
    st.success("AWS credentials successfully loaded!")
else:
    st.error("Failed to load AWS credentials.")

# Page Content
if choice == "🏠 Home":
    st.subheader("Welcome to Cloud Automation Training! 🎉")
    st.write("Learn how to automate cloud resources with Python and Terraform.")
    logging.debug("Home Page Loaded.")

elif choice == "📊 Dashboard":
    st.subheader("📊 Dashboard")
    st.write("This is where your cloud automation metrics will be displayed.")
    logging.debug("Dashboard Page Loaded.")

elif choice == "🛠️ Terraform Automation":
    st.subheader("🛠️ Terraform Automation")
    st.write("Manage your Terraform infrastructure here.")
    logging.debug("Terraform Automation Page Loaded.")

elif choice == "👤 About":
    st.subheader("👤 About the Author")
    st.write("""
        **Emen Ufeh** is a passionate cloud automation engineer dedicated to delivering modern, scalable solutions. 
        With expertise in Python, Terraform, and AWS, Emen has contributed to several automation projects that have 
        streamlined cloud infrastructure management.
    """)
    st.write("Visit [GitHub](https://github.com/Emenlentino) for more projects and contributions.")
    logging.debug("About Page Loaded.")

elif choice == "📞 Contact":
    st.subheader("📞 Contact")
    st.write("""
        For inquiries or support, feel free to reach out:
        - **Email**: emenlentino@gmail.com
        - **GitHub**: [github.com/Emenlentino](https://github.com/Emenlentino)
    """)
    st.write("We are here to assist you with all your cloud automation needs!")
    logging.debug("Contact Page Loaded.")
