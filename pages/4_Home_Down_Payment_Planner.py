# pages/4_Home_Down_Payment_Planner.py

import streamlit as st
from datetime import datetime, timedelta
import math

st.set_page_config(layout="centered")
st.title("🏡 Home Down Payment Planner")

# Step 1: Get base inputs
st.subheader("📋 Step 1: Enter Your Home Buying Goal")
house_price = st.number_input("Target House Price ($)", min_value=10000, value=300000, step=1000)
down_percent = st.slider("Down Payment Percentage", 0, 100, value=20, step=1)

down_payment = house_price * (down_percent / 100)
st.markdown(f"💰 **Target Down Payment:** ${down_payment:,.2f}")

# Step 2: Choose planning mode
st.subheader("📅 Step 2: Plan Your Savings")
mode = st.radio("Do you want to:", ["Pick a date to reach your goal", "Pick a monthly savings amount"])

if mode == "Pick a date to reach your goal":
    goal_date = st.date_input("Select your savings goal date", value=datetime.today() + timedelta(days=365))
    months_remaining = max((goal_date.year - datetime.today().year) * 12 + (goal_date.month - datetime.today().month), 1)

    monthly_target = down_payment / months_remaining
    st.success(f"💸 You need to save **${monthly_target:,.2f}/month** to reach your goal by {goal_date.strftime('%B %Y')}.")

elif mode == "Pick a monthly savings amount":
    monthly_savings = st.number_input("How much can you save each month?", min_value=50.0, value=1000.0, step=50.0)
    if monthly_savings > 0:
        months_needed = math.ceil(down_payment / monthly_savings)
        projected_date = datetime.today() + timedelta(days=months_needed * 30)
        st.success(f"📆 You'll reach your goal in about **{months_needed} months**, around {projected_date.strftime('%B %Y')}.")

# Optional: Anchor message
st.markdown("---")
st.markdown("### 🧠 Emotional Anchor")
st.markdown("> _“Every dollar saved is a brick in your family’s foundation. This is not pressure—this is preparation.”_")
