# app/main.py
import streamlit as st
from app.components.navigation import create_navigation
from app.components.auth import check_authentication
from app.database.mongodb_client import db

def main():
    st.set_page_config(
        page_title="CloudwithDevesh",
        page_icon="☁️",
        layout="wide"
    )
    
    # Initialize session state
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    
    # Create navigation
    create_navigation()
    
    # Check authentication
    if not check_authentication():
        st.warning("Please log in to access all features")
        return
    
    # Main content area
    st.title("Welcome to CloudwithDevesh")
    st.write("Your one-stop platform for tech learning and mentorship")

if __name__ == "__main__":
    main()