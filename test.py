import joblib
import pandas as pd

# Load the model
model = joblib.load("./model/model_rf.pkl")

# Create a test input
test_input = pd.DataFrame({
    "Age": [21],
    "Gender": [1],  # Male
    "Heart_Rate": [99],
    "Blood_Pressure_Systolic": [165],
    "Blood_Pressure_Diastolic": [107],
    "Stress_Level_Biosensor": [9],
    "Stress_Level_Self_Report": [9],
    "Physical_Activity": [2],  # Medium
    "Sleep_Quality": [0],  # Medium
    "Mood": [0],  # Medium
    "Study_Hours": [60],
    "Project_Hours": [32]
})

# Predict
prediction = model.predict(test_input)
print("Prediction:", prediction)