# import joblib
# import pandas as pd

# model = joblib.load("./model/model_rf.pkl")

# test_input = pd.DataFrame({
#     "Age": [21],
#     "Gender": [1],  
#     "Heart_Rate": [99],
#     "Blood_Pressure_Systolic": [165],
#     "Blood_Pressure_Diastolic": [107],
#     "Stress_Level_Biosensor": [9],
#     "Stress_Level_Self_Report": [9],
#     "Physical_Activity": [2],  
#     "Sleep_Quality": [0],  
#     "Mood": [0], 
#     "Study_Hours": [60],
#     "Project_Hours": [32]
# })

# prediction = model.predict(test_input)
# print("Prediction:", prediction)

from model import predict_risk
import pandas as pd

test_input = pd.DataFrame({
    "Age": [21],
    "Gender": [1],
    "Heart_Rate": [99],
    "Blood_Pressure_Systolic": [165],
    "Blood_Pressure_Diastolic": [107],
    "Stress_Level_Biosensor": [9],
    "Stress_Level_Self_Report": [9],
    "Physical_Activity": [2],
    "Sleep_Quality": [0],
    "Mood": [0],
    "Study_Hours": [60],
    "Project_Hours": [32]
})

print("Prediction:", predict_risk(test_input))
