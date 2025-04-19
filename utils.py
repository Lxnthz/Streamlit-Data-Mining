import streamlit as st
import pandas as pd

def collect_user_input():
    age = st.number_input("Age", 10, 100, 20)
    gender = st.selectbox("Gender", ["M", "F"])
    heart_rate = st.slider("Heart Rate", 40, 180, 70)
    systolic = st.slider("Systolic BP", 80, 180, 120)
    diastolic = st.slider("Diastolic BP", 50, 120, 80)
    stress_bio = st.slider("Stress (Biosensor)", 0.0, 10.0, 5.0)
    stress_self = st.slider("Stress (Self Report)", 0.0, 10.0, 5.0)
    activity = st.selectbox("Activity Level", ["High", "Moderate", "Low"])
    sleep = st.selectbox("Sleep Quality", ["Good", "Moderate", "Poor"])
    mood = st.selectbox("Mood", ["Happy", "Stressed", "Anxious"])
    study = st.number_input("Study Hours", 0.0, 100.0, 20.0)
    project = st.number_input("Project Hours", 0.0, 100.0, 10.0)

    input_dict = {
        "Age": age,
        "Gender": gender,
        "Heart_Rate": heart_rate,
        "Blood_Pressure_Systolic": systolic,
        "Blood_Pressure_Diastolic": diastolic,
        "Stress_Level_Biosensor": stress_bio,
        "Stress_Level_Self_Report": stress_self,
        "Physical_Activity": activity,
        "Sleep_Quality": sleep,
        "Mood": mood,
        "Study_Hours": study,
        "Project_Hours": project
    }

    return pd.DataFrame([input_dict])
