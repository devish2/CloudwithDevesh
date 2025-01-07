# app/pages/home.py
import streamlit as st
from app.utils.styling import apply_custom_styling

def show_home():
    apply_custom_styling()
    
    # Hero Section
    st.markdown('<h1 class="main-header">CloudwithDevesh</h1>', unsafe_allow_html=True)
    
    # Hero content with gradient background
    st.markdown("""
        <div style="
            background: linear-gradient(45deg, #2193b0, #6dd5ed);
            padding: 3rem;
            border-radius: 1rem;
            color: white;
            margin-bottom: 2rem;
        ">
            <h2 style="font-size: 2.5rem; margin-bottom: 1rem;">Transform Your Tech Career</h2>
            <p style="font-size: 1.2rem; margin-bottom: 2rem;">
                Get personalized mentorship, access curated roadmaps, and learn from industry experts.
            </p>
            <button style="
                background: white;
                color: #2193b0;
                border: none;
                padding: 0.8rem 2rem;
                border-radius: 0.5rem;
                font-weight: 600;
                cursor: pointer;
            ">
                Book Free Trial Session
            </button>
        </div>
    """, unsafe_allow_html=True)
    
    # Featured Programs
    st.subheader("Featured Programs")
    
    col1, col2, col3 = st.columns(3)
    
    # Custom card component
    def create_feature_card(title, description, icon, col):
        with col:
            st.markdown(f"""
                <div style="
                    background: white;
                    padding: 1.5rem;
                    border-radius: 1rem;
                    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                    height: 100%;
                    text-align: center;
                ">
                    <div style="font-size: 3rem; color: #2193b0; margin-bottom: 1rem;">
                        {icon}
                    </div>
                    <h3 style="margin-bottom: 1rem; color: #333;">{title}</h3>
                    <p style="color: #666;">{description}</p>
                </div>
            """, unsafe_allow_html=True)
    
    create_feature_card(
        "Tech Roadmaps",
        "Follow structured learning paths designed for your success",
        "🗺️",
        col1
    )
    
    create_feature_card(
        "Video Tutorials",
        "Learn from comprehensive video content and hands-on demos",
        "🎥",
        col2
    )
    
    create_feature_card(
        "1:1 Mentorship",
        "Get personalized guidance from experienced professionals",
        "👨‍🏫",
        col3
    )
    
    # Latest Content Section
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.subheader("Latest Content")
    
    # Create tabs for different content types
    tabs = st.tabs(["Recent Videos", "Popular Roadmaps", "Upcoming Sessions"])
    
    with tabs[0]:
        col1, col2 = st.columns(2)
        with col1:
            st.video("https://youtube.com/watch?v=your_video_id")
        with col2:
            st.markdown("""
                <div style="padding: 1rem;">
                    <h3>Latest Video Title</h3>
                    <p>Description of the video goes here...</p>
                    <div style="margin-top: 1rem;">
                        <span style="background: #e0e0e0; padding: 0.3rem 0.6rem; border-radius: 1rem; margin-right: 0.5rem;">
                            #Python
                        </span>
                        <span style="background: #e0e0e0; padding: 0.3rem 0.6rem; border-radius: 1rem;">
                            #WebDev
                        </span>
                    </div>
                </div>
            """, unsafe_allow_html=True)

# Let's create an enhanced mentorship booking page:

# ```python
# app/pages/mentorship.py
import streamlit as st
from app.utils.styling import apply_custom_styling

def show_mentorship():
    apply_custom_styling()
    
    st.markdown('<h1 class="main-header">Mentorship Programs</h1>', unsafe_allow_html=True)
    
    # Program cards
    col1, col2, col3 = st.columns(3)
    
    def create_program_card(title, duration, price, features, col):
        with col:
            st.markdown(f"""
                <div style="
                    background: white;
                    padding: 2rem;
                    border-radius: 1rem;
                    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                    text-align: center;
                ">
                    <h3 style="color: #2193b0; font-size: 1.5rem; margin-bottom: 1rem;">
                        {title}
                    </h3>
                    <div style="
                        font-size: 2.5rem;
                        font-weight: 700;
                        margin: 1rem 0;
                        color: #333;
                    ">
                        ₹{price}
                    </div>
                    <div style="color: #666; margin-bottom: 1rem;">
                        {duration} Duration
                    </div>
                    <ul style="
                        list-style: none;
                        padding: 0;
                        text-align: left;
                        margin-bottom: 2rem;
                    ">
                        {"".join([f'<li style="margin-bottom: 0.5rem;">✓ {feature}</li>' for feature in features])}
                    </ul>
                    <button style="
                        background: linear-gradient(45deg, #2193b0, #6dd5ed);
                        color: white;
                        border: none;
                        padding: 0.8rem 2rem;
                        border-radius: 0.5rem;
                        font-weight: 600;
                        width: 100%;
                        cursor: pointer;
                    ">
                        Choose Plan
                    </button>
                </div>
            """, unsafe_allow_html=True)
    
    create_program_card(
        "Starter",
        "1 Month",
        "999",
        [
            "4 One-on-one Sessions",
            "Access to Learning Resources",
            "Email Support",
            "Career Guidance"
        ],
        col1
    )
    
    create_program_card(
        "Professional",
        "3 Months",
        "2499",
        [
            "12 One-on-one Sessions",
            "Priority Support",
            "Custom Learning Path",
            "Resume Review",
            "Mock Interviews"
        ],
        col2
    )
    
    create_program_card(
        "Enterprise",
        "6 Months",
        "4499",
        [
            "24 One-on-one Sessions",
            "24/7 Priority Support",
            "Custom Project Guidance",
            "Job Referrals",
            "LinkedIn Profile Review",
            "Interview Preparation"
        ],
        col3
    )
    
    # Booking Form
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.subheader("Book Your Session")
    
    with st.form("booking_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("Full Name")
            email = st.text_input("Email Address")
        
        with col2:
            phone = st.text_input("Phone Number")
            program = st.selectbox(
                "Select Program",
                ["Starter (1 Month)", "Professional (3 Months)", "Enterprise (6 Months)"]
            )
        
        st.text_area("What are your learning goals?")
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            submitted = st.form_submit_button("Book Now")

# Let's create a roadmap page with interactive elements:

# ```python
# app/pages/roadmaps.py
import streamlit as st
from app.utils.styling import apply_custom_styling

def show_roadmaps():
    apply_custom_styling()
    
    st.markdown('<h1 class="main-header">Tech Roadmaps</h1>', unsafe_allow_html=True)
    
    # Search and filter section
    col1, col2 = st.columns([3, 1])
    with col1:
        search = st.text_input("Search roadmaps...")
    with col2:
        category = st.selectbox(
            "Category",
            ["All", "Web Development", "Data Science", "DevOps", "Mobile Development"]
        )
    
    # Roadmap cards
    def create_roadmap_card(title, description, difficulty, duration, topics):
        st.markdown(f"""
            <div style="
                background: white;
                padding: 1.5rem;
                border-radius: 1rem;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                margin-bottom: 1rem;
            ">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <h3 style="color: #2193b0; margin: 0;">{title}</h3>
                    <div>
                        <span style="
                            background: #e0e0e0;
                            padding: 0.3rem 0.6rem;
                            border-radius: 1rem;
                            font-size: 0.8rem;
                            margin-right: 0.5rem;
                        ">
                            {difficulty}
                        </span>
                        <span style="
                            background: #e0e0e0;
                            padding: 0.3rem 0.6rem;
                            border-radius: 1rem;
                            font-size: 0.8rem;
                        ">
                            {duration}
                        </span>
                    </div>
                </div>
                <p style="color: #666; margin: 1rem 0;">{description}</p>
                <div style="display: flex; flex-wrap: wrap; gap: 0.5rem;">
                    {"".join([f'<span style="background: #f0f0f0; padding: 0.3rem 0.6rem; border-radius: 1rem; font-size: 0.8rem;">{topic}</span>' for topic in topics])}
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    # Sample roadmap cards
    create_roadmap_card(
        "Full Stack Web Development",
        "Complete guide to becoming a full stack web developer",
        "Intermediate",
        "6 months",
        ["HTML/CSS", "JavaScript", "React", "Node.js", "MongoDB", "AWS"]
    )
    
    create_roadmap_card(
        "Python for Data Science",
        "Master Python for data analysis and machine learning",
        "Beginner",
        "4 months",
        ["Python", "Pandas", "NumPy", "Scikit-learn", "TensorFlow"]
    )

# These pages showcase a modern, professional design with:

# 1. Consistent color scheme and styling
# 2. Responsive layouts using columns
# 3. Custom cards and components
# 4. Interactive elements
# 5. Clear typography and spacing
# 6. Gradient backgrounds and hover effects
# 7. Mobile-friendly design

# Would you like me to continue with the design for:

# 1. Video tutorials page
# 2. User dashboard
# 3. Course catalog
# 4. Profile settings
# 5. Admin panel

# Let me know which sections you'd like to see next!