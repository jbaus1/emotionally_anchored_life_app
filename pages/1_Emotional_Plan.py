# pages/1_Emotional_Plan.py

import streamlit as st

st.title("🧠 Emotionally Anchored Life Plan")

mantras = [
    "This is chemistry, not character.",
    "I am not behind. I am building.",
    "My family needs me, not perfection.",
    "This isn’t the end of my story. I’m still writing it."
]

st.markdown("### 💬 Mantras")
for m in mantras:
    st.markdown(f"- {m}")

# Goals
goals = {
    "🏡 Buy a Home": [
        "Review current savings and credit score",
        "Estimate down payment and closing costs",
        "Research loan types",
        "Identify school districts",
        "Make a Home Readiness checklist"
    ],
    "🏫 Right School for My Son": [
        "Stay in contact with the special school district",
        "Journal how he's adjusting",
        "Research future school districts"
    ],
    "💵 Build Financial Stability": [
        "Create bill flow map",
        "Set up financial buckets",
        "Review and cut unused expenses",
        "Automate small weekly savings"
    ],
    "🧠 Mental Health Consistency": [
        "Daily meds reminder",
        "5-min evening reset ritual",
        "Display mantras visibly",
        "Track spirals and patterns"
    ]
}

st.markdown("### 🎯 Goals and Micro-Steps")
for goal, tasks in goals.items():
    st.subheader(goal)
    for task in tasks:
        st.checkbox(task, key=f"{goal}_{task}")
