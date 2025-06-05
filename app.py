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

# Step 3: Sport-Specific Stats
st.header("Step 3: Your Performance Stats")
match_score = 0

if sport.lower() == "basketball":
    ppg = st.number_input("Points Per Game", 0.0, 50.0, step=0.1)
    apg = st.number_input("Assists Per Game", 0.0, 15.0, step=0.1)
    rpg = st.number_input("Rebounds Per Game", 0.0, 20.0, step=0.1)
    match_score += ppg + apg + rpg
elif sport.lower() == "football":
    dash_40 = st.number_input("40-Yard Dash (seconds)", 3.5, 6.0, step=0.01)
    tackles = st.number_input("Total Tackles", 0, 200)
    passing_yards = st.number_input("Passing Yards (QB only)", 0, 5000)
    match_score += (200 - dash_40 * 30) + tackles + passing_yards / 100
elif sport.lower() == "soccer":
    goals = st.number_input("Goals Scored", 0, 100)
    assists = st.number_input("Assists", 0, 100)
    minutes = st.number_input("Minutes Played", 0, 5000)
    match_score += goals + assists + minutes / 100
elif sport.lower() == "baseball":
    avg = st.number_input("Batting Average", 0.0, 1.0, step=0.001)
    home_runs = st.number_input("Home Runs", 0, 100)
    rbi = st.number_input("RBIs", 0, 200)
    match_score += avg * 100 + home_runs + rbi
elif sport.lower() == "track":
    sprint_100m = st.number_input("100m Dash Time (seconds)", 9.0, 20.0, step=0.01)
    sprint_200m = st.number_input("200m Dash Time (seconds)", 18.0, 40.0, step=0.01)
    match_score += (40 - sprint_100m) + (40 - sprint_200m)
elif sport.lower() == "esports":
    game = st.text_input("Primary Game (e.g., Fortnite, Valorant, Rocket League)")
    rank = st.text_input("Rank or Tier (e.g., Gold, Diamond, Top 1%):")
    hours = st.number_input("Hours Played (total)", 0, 10000)
    win_rate = st.slider("Win Rate (%)", 0, 100, 50)
    match_score += win_rate + hours / 100
else:
    st.info("Enter a recognized high school sport to see tailored stats.")

# Step 4: School Preferences
st.header("Step 4: What Type of School Interests You Most?")
level = st.selectbox("Choose one:", ["NCAA D1", "NCAA D2", "NCAA D3", "NAIA", "JUCO", "Undecided"])
region = st.multiselect("Preferred Region(s):", ["East Coast", "West Coast", "South", "Midwest", "Anywhere"]) 

# Step 5: Top 3 Opportunity Matches (Demo Static Output)
st.header("Step 5: Top 3 Demo College Matches")
st.markdown("""
1. **Southern State University** – JUCO, Strong Fit, High Playing Time Potential  
2. **Northbridge College** – NCAA D3, Academic-Athletic Balance, Coach Openings  
3. **Coastal Tech** – NCAA D2, Interested in athletes from your position
""")

# Step 6: Delivery
st.header("Step 6: Where Should We Send Updates?")
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
    **Match Strength Score:** {round(match_score, 2)}  
    **Delivery Method:** {delivery_method} → {contact_info}
    """)
    st.info("Magic says: The right match can change everything. Let’s keep you visible.")
    st.balloons()
