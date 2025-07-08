# financial_tracker.py

import streamlit as st
import pandas as pd

st.subheader("💰 Financial Tracker: Budget Flow + Emotional Anchors")

# 1. Monthly Income
income = st.number_input("💵 Monthly Income (After Taxes):", min_value=0, value=4000, step=100)

# 2. Expenses Table
st.markdown("### 🧾 Monthly Expenses")
default_expenses = {
    "Rent/Mortgage": 1500,
    "Tuition": 800,
    "Utilities": 250,
    "Groceries": 500,
    "Student Loan Savings": 300,
    "Misc": 200
}

expense_data = {}
for category, default in default_expenses.items():
    expense_data[category] = st.number_input(f"{category}:", min_value=0, value=default, step=50)

# 3. Summary
total_expenses = sum(expense_data.values())
leftover = income - total_expenses

st.markdown("---")
st.markdown(f"### 📊 Summary")
st.markdown(f"**Total Expenses:** ${total_expenses}")
st.markdown(f"**Leftover for Savings/Flex:** ${leftover}")

# 4. Emotional Anchors
st.markdown("---")
st.markdown("### 🧠 Emotional Anchor")
if leftover < 0:
    st.error("You're over budget—pause and reflect with compassion.")
    st.markdown("> _“This is information, not failure. I can adjust.”_")
elif leftover < 100:
    st.warning("Tight margin. Consider reducing one expense slightly.")
    st.markdown("> _“Small shifts can change my direction.”_")
else:
    st.success("You've got surplus to work with. Well done.")
    st.markdown("> _“I am not behind—I am building.”_")

