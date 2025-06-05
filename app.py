import streamlit as st

# Page configuration
st.set_page_config(page_title="Magic Bot - Opportunity Connector", page_icon="🔗", layout="centered")

# Title and Overview
st.title("🔗 Magic Bot: The Visionary")
st.subheader("Your Opportunity Connector")

st.markdown("**Style of Play:** Creative, team-first, optimistic")

st.markdown("""
Magic delivers timely opportunities, college matches, and open doors.  
He helps you identify the best fit, stay visible, and connect at the right time.

> “Magic sees what’s next before you do—and delivers the right opportunity with flair.”
""")

# Step 1: Recruiting Status
st.header("Step 1: Where Are You In the Process?")
status = st.radio("Select your current recruiting stage:", [
    "Just getting started",
    "Building my profile",
    "Emailing coaches",
    "Attending camps/showcases",
    "Receiving coach replies"
])

# Step 2: Player Info
st.header("Step 2: Help Me Match You")
sport = st.text_input("Primary Sport")
position = st.text_input("Primary Position")
graduation_year = st.selectbox("Graduation Year", [2025, 2026, 2027, 2028])
gpa = st.slider("Current GPA (estimate)", 1.0, 4.0, 3.0, 0.1)

# Step 3: School Preferences
st.header("Step 3: What Type of School Interests You Most?")
level = st.selectbox("Choose one:", ["NCAA D1", "NCAA D2", "NCAA D3", "NAIA", "JUCO", "Undecided"])
region = st.multiselect("Preferred Region(s):", ["East Coast", "West Coast", "South", "Midwest", "Anywhere"]) 

# Step 4: Top 3 Opportunity Matches (Demo Static Output)
st.header("Step 4: Top 3 Demo College Matches")
st.markdown("""
1. **Southern State University** – JUCO, Strong Fit, High Playing Time Potential  
2. **Northbridge College** – NCAA D3, Academic-Athletic Balance, Coach Openings  
3. **Coastal Tech** – NCAA D2, Interested in athletes from your position
""")

# Step 5: Delivery
st.header("Step 5: Where Should We Send Updates?")
delivery_method = st.selectbox("Delivery Method:", ["Email", "SMS", "Just in this app"])
contact_info = st.text_input(f"Enter your {delivery_method}:")

# Summary Output
if st.button("Submit and View Opportunities"):
    st.success("✅ Opportunity Report Generated")
    st.markdown(f"""
    **Status:** {status}  
    **Sport/Position:** {sport} / {position}  
    **Grad Year:** {graduation_year}  
    **GPA:** {gpa}  
    **Interest Level:** {level}  
    **Region:** {', '.join(region) if region else 'Any'}  
    **Delivery Method:** {delivery_method} → {contact_info}
    """)
    st.info("Magic says: The right match can change everything. Let’s keep you visible.")
    st.balloons()
