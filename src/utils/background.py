import base64
import logging
import streamlit as st

def get_base64_of_bin_file(bin_file):
    """
    Read a binary file (image) and convert it to a base64 string for embedding.
    """
    try:
        with open(bin_file, "rb") as f:
            data = f.read()
        logging.debug(f"Loaded image {bin_file} successfully.")
        return base64.b64encode(data).decode()
    except Exception as e:
        logging.error(f"Error reading file {bin_file}: {str(e)}")
        return None

def set_background(png_file):
    """
    Set the background image for the Streamlit app.
    """
    bin_str = get_base64_of_bin_file(png_file)
    if bin_str:
        page_bg_img = f'''
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{bin_str}");
            background-size: cover;
        }}
        </style>
        '''
        st.markdown(page_bg_img, unsafe_allow_html=True)
    else:
        logging.error("Failed to set background image.")
