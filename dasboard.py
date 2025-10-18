import streamlit as st
import pandas as pd
from src.agent import WaterInTakeAgent
from src.database import log_intake, intake_history, init_db

st.title("💧 AI Water Tracker Dashboard")

init_db()

user_id = st.sidebar.text_input("👤 Enter User ID", value="user_123")
intake_ml = st.sidebar.number_input("💦 Enter water intake (ml)", min_value=0, step=100)

if st.button("Log Intake"):
    log_intake(user_id, intake_ml)
    agent = WaterInTakeAgent()
    feedback = agent.AnalyzeWaterIntake(intake_ml)
    st.success(f"✅ {intake_ml} ml logged for {user_id}")
    st.info(f"🤖 AI Suggestion: {feedback}")

if st.button("View History"):
    data = intake_history(user_id)
    if data:
        df = pd.DataFrame(data, columns=["ID", "User ID", "Date", "Intake (ml)"])
        st.dataframe(df)
        st.area_chart(df, x="Date", y="Intake (ml)")
    else:
        st.warning("⚠️ No records found for this user.")
