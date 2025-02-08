import logging
import streamlit as st

def fetch_aws_credentials():
    """
    Fetch AWS credentials from Streamlit secrets.
    """
    access_key = st.secrets.get("AWS_ACCESS_KEY_ID", None)
    secret_key = st.secrets.get("AWS_SECRET_ACCESS_KEY", None)

    if access_key and secret_key:
        logging.debug("AWS credentials successfully fetched from Streamlit secrets.")
        return access_key, secret_key
    else:
        logging.error("AWS credentials not found in Streamlit secrets.")
        return None, None

def request_user_credentials():
    """
    Request AWS credentials from the user if secrets are not found.
    """
    access_key = st.text_input("🔑 AWS Access Key", key="aws_access_key", value="")
    secret_key = st.text_input("🔑 AWS Secret Key", key="aws_secret_key", value="", type="password")
    
    if access_key and secret_key:
        logging.debug("AWS credentials successfully provided by the user.")
        return access_key, secret_key
    else:
        logging.warning("AWS credentials not provided by user.")
        return None, None
