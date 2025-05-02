import streamlit as st
import pandas as pd

def collect_user_input():
    age = st.number_input("Umur (18-24)", min_value=18, max_value=24, value=21)
    gender = st.selectbox("Jenis Kelamin (Female/Male)", ["Female", "Male"])
    heart_rate = st.number_input("Heart Rate (50-99)", min_value=50, max_value=99, value=75)
    blood_pressure_systolic = st.number_input("Blood Pressure Systolic (90-165)", min_value=90, max_value=165, value=120)
    blood_pressure_diastolic = st.number_input("Blood Pressure Diastolic (60-107)", min_value=60, max_value=107, value=80)
    stress_biosensor = st.slider("Stress Level (Biosensor, 1-9)", min_value=1, max_value=9, value=5)
    stress_report = st.slider("Stress Level (Self-Report, 1-9)", min_value=1, max_value=9, value=5)
    physical_activity = st.selectbox("Physical Activity", ["Low", "Medium", "High"], index=1)
    sleep_quality = st.selectbox("Sleep Quality", ["Low", "Medium", "High"], index=1)
    mood = st.selectbox("Mood", ["Low", "Medium", "High"], index=1)
    study_hours = st.number_input("Study Hours (5-60)", min_value=5, max_value=60, value=20)
    project_hours = st.number_input("Project Hours (0-32)", min_value=0, max_value=32, value=10)

    gender_encoded = 0 if gender == "Female" else 1
    physical_activity_encoded = {"Low": 1, "Medium": 2, "High": 0}[physical_activity]
    sleep_quality_encoded = {"Low": 1, "Medium": 2, "High": 0}[sleep_quality]
    mood_encoded = {"Low": 1, "Medium": 2, "High": 0}[mood]

    input_data = {
        "Age": [age],
        "Gender": [gender_encoded], 
        "Heart_Rate": [heart_rate],
        "Blood_Pressure_Systolic": [blood_pressure_systolic],
        "Blood_Pressure_Diastolic": [blood_pressure_diastolic],
        "Stress_Level_Biosensor": [stress_biosensor],
        "Stress_Level_Self_Report": [stress_report],
        "Physical_Activity": [physical_activity_encoded], 
        "Sleep_Quality": [sleep_quality_encoded], 
        "Mood": [mood_encoded], 
        "Study_Hours": [study_hours],
        "Project_Hours": [project_hours],
    }
    return pd.DataFrame(input_data)