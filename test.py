import joblib
import pandas as pd

# Load the model
model = joblib.load("./model/model_rf.pkl")

# Create a test input
test_input = pd.DataFrame({
    "Age": [21],
    "Gender": [1],  # Male
    "Heart_Rate": [75],
    "Blood_Pressure_Systolic": [120],
    "Blood_Pressure_Diastolic": [80],
    "Stress_Level_Biosensor": [5],
    "Stress_Level_Self_Report": [5],
    "Physical_Activity": [1],  # Medium
    "Sleep_Quality": [1],  # Medium
    "Mood": [1],  # Medium
    "Study_Hours": [20],
    "Project_Hours": [10]
})

# Predict
prediction = model.predict(test_input)
print("Prediction:", prediction)