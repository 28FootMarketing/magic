import streamlit as st

st.set_page_config(page_title="Magic Bot - Opportunity Connector", page_icon="🔗", layout="centered")

st.title("🔗 Magic Bot: The Visionary")
st.subheader("Your Opportunity Connector")

st.markdown("**Style of Play:** Creative, team-first, optimistic")

st.markdown("""
Magic delivers timely opportunities, college matches, and open doors.  
He helps you identify the best fit, stay visible, and connect at the right time.

> “Magic sees what’s next before you do—and delivers the right opportunity with flair.”
""")

st.header("Step 1: Where Are You In the Process?")
status = st.radio("Select your current recruiting stage:", [
    "Just getting started",
    "Building my profile",
    "Emailing coaches",
    "Attending camps/showcases",
    "Receiving coach replies"
])

sports_positions_stats = {
    "Basketball": {
        "positions": ["Point Guard", "Shooting Guard", "Small Forward", "Power Forward", "Center"],
        "stats": ["Points Per Game", "Assists", "Rebounds", "Steals", "Blocks"]
    },
    "Football": {
        "positions": ["Quarterback", "Running Back", "Wide Receiver", "Linebacker", "Defensive Back"],
        "stats": ["Passing Yards", "Rushing Yards", "Receptions", "Tackles", "Interceptions"]
    },
    "Girls Flag Football": {
        "positions": ["Quarterback", "Running Back", "Receiver", "Safety", "Linebacker"],
        "stats": ["Completions", "Yards Thrown", "Touchdowns", "Flag Pulls", "Interceptions"]
    },
    "Soccer": {
        "positions": ["Goalkeeper", "Defender", "Midfielder", "Forward"],
        "stats": ["Goals", "Assists", "Pass Accuracy", "Tackles", "Saves"]
    },
    "Baseball": {
        "positions": ["Pitcher", "Catcher", "Infielder", "Outfielder"],
        "stats": ["Batting Average", "Home Runs", "RBIs", "Stolen Bases", "ERA"]
    },
    "Track & Field": {
        "positions": ["Sprinter", "Distance Runner", "Jumper", "Thrower"],
        "stats": ["100m Time", "200m Time", "Long Jump", "Shot Put", "Discus"]
    },
    "Esports": {
        "positions": ["FPS Player", "MOBA Player", "Strategist", "Support"],
        "stats": ["K/D Ratio", "Win Rate", "Avg Score", "Headshot %", "Hours Played"]
    }
}

st.header("Step 2: Choose Your Sport")
sport = st.selectbox("Select Your Sport", list(sports_positions_stats.keys()))

position = st.selectbox("Select Your Position", sports_positions_stats[sport]["positions"])

st.header("Step 3: Enter Your Performance Stats")
user_stats = {}
match_score = 0

for stat in sports_positions_stats[sport]["stats"]:
    value = st.number_input(f"{stat}", value=0.0)
    user_stats[stat] = value
    match_score += value if isinstance(value, (int, float)) else 0

st.header("Step 4: Academic and Personal Info")
graduation_year = st.selectbox("Graduation Year", [2025, 2026, 2027, 2028])
gpa = st.slider("GPA (Estimate)", 1.0, 4.0, 3.0, 0.1)

st.header("Step 5: School Preferences")
level = st.selectbox("Target Level", ["NCAA D1", "NCAA D2", "NCAA D3", "NAIA", "JUCO", "Undecided"])
region = st.multiselect("Preferred Region(s):", ["East Coast", "West Coast", "South", "Midwest", "Anywhere"])

st.header("Step 6: Delivery Option")
delivery_method = st.selectbox("Delivery Method:", ["Email", "SMS", "In-App Only"])
contact_info = st.text_input(f"Enter your {delivery_method}:")

if st.button("Submit and Get My Matches"):
    st.success("✅ Your opportunity profile has been generated!")
    st.markdown(f"""
    **Sport/Position:** {sport} - {position}  
    **Stats Summary:** {user_stats}  
    **Graduation Year:** {graduation_year}  
    **GPA:** {gpa}  
    **Target Level:** {level}  
    **Region Preference:** {', '.join(region)}  
    **Delivery:** {delivery_method} → {contact_info}  
    **Match Strength Score:** {round(match_score, 2)}
    """)
    st.info("Magic says: When preparation meets opportunity, success is born. Let's get visible.")
    st.balloons()
