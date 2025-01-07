# app/utils/styling.py
import streamlit as st

def apply_custom_styling():
    # Custom CSS for modern look and feel
    st.markdown("""
        <style>
        /* Main container */
        .main {
            padding: 2rem;
        }
        
        /* Custom card styling */
        .stCard {
            border-radius: 1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: transform 0.2s;
            background: white;
        }
        
        .stCard:hover {
            transform: translateY(-5px);
        }
        
        /* Custom button styling */
        .stButton>button {
            border-radius: 0.5rem;
            padding: 0.5rem 2rem;
            font-weight: 600;
            background: linear-gradient(45deg, #2193b0, #6dd5ed);
            border: none;
            color: white;
        }
        
        /* Header styling */
        .main-header {
            font-size: 3rem;
            font-weight: 700;
            background: linear-gradient(45deg, #2193b0, #6dd5ed);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 2rem;
        }
        
        /* Navigation menu */
        .nav-link {
            text-decoration: none;
            color: #333;
            padding: 0.5rem 1rem;
            border-radius: 0.5rem;
            transition: background-color 0.2s;
        }
        
        .nav-link:hover {
            background-color: #f0f0f0;
        }
        
        /* Custom containers */
        .content-container {
            background: white;
            padding: 2rem;
            border-radius: 1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        </style>
    """, unsafe_allow_html=True)