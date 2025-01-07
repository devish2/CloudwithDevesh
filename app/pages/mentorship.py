# app/pages/mentorship.py
import streamlit as st
from datetime import datetime, timedelta
from app.database.mongodb_client import db
from app.services.link_service import create_payment_link

def show_mentorship():
    st.title("Mentorship Programs")
    
    # Program selection
    program_type = st.selectbox(
        "Choose your mentorship program",
        ["1 Month", "3 Months", "6 Months"]
    )
    
    # Pricing information
    pricing = {
        "1 Month": 999,
        "3 Months": 2499,
        "6 Months": 4499
    }
    
    st.write(f"Program Price: ₹{pricing[program_type]}")
    
    # Booking form
    with st.form("booking_form"):
        name = st.text_input("Full Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone Number")
        goals = st.text_area("What are your learning goals?")
        
        submitted = st.form_submit_button("Book Now")
        
        if submitted:
            # Create booking in MongoDB
            booking = {
                "name": name,
                "email": email,
                "phone": phone,
                "goals": goals,
                "program_type": program_type,
                "amount": pricing[program_type],
                "status": "pending",
                "created_at": datetime.now()
            }
            
            booking_id = db.get_collection("bookings").insert_one(booking).inserted_id
            
            # Create payment link
            payment_link = create_payment_link(
                amount=pricing[program_type],
                description=f"Mentorship Program - {program_type}",
                customer_name=name,
                customer_email=email,
                booking_id=str(booking_id)
            )
            
            st.success("Booking created successfully!")
            st.markdown(f"[Proceed to Payment]({payment_link})")

if __name__ == "__main__":
    show_mentorship()