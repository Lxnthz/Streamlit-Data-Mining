# import joblib
# import pandas as pd

# def load_model():
#     model = joblib.load("./model/mlp_model.pkl")
#     return model 

# def predict_risk(input_data):
#     model = load_model()
#     prediction = model.predict(input_data)[0]
#     risk_mapping = {
#         1: "Low Risk",
#         2: "Medium Risk",
#         0: "High Risk"
#     }
#     return risk_mapping.get(prediction, "Unknown Risk")

import joblib
import pandas as pd

# Load model dan scaler
mlp_model = joblib.load("./model/mlp_model.pkl")
scaler = joblib.load("./model/scaler.pkl")

# Fitur yang digunakan oleh model MLP
mlp_features = ['Stress_Level_Biosensor', 'Stress_Level_Self_Report', 'Sleep_Quality',
                'Physical_Activity', 'Gender', 'Age']

# Fitur yang perlu dinormalisasi
features_to_normalize = ['Age','Heart_Rate', 'Blood_Pressure_Systolic', 'Blood_Pressure_Diastolic',
                         'Stress_Level_Biosensor', 'Stress_Level_Self_Report', 
                         'Study_Hours', 'Project_Hours']

def preprocess_input(input_df):
    # Normalisasi hanya fitur tertentu
    normalized_values = scaler.transform(input_df[features_to_normalize])
    normalized_df = pd.DataFrame(normalized_values, columns=features_to_normalize)

    # Ganti kolom yang dinormalisasi ke input_df
    input_df.update(normalized_df)

    # Ambil fitur yang sesuai model
    final_input = input_df[mlp_features]
    return final_input

def predict_risk(input_df):
    processed_input = preprocess_input(input_df)
    prediction = mlp_model.predict(processed_input)[0]
    risk_mapping = {
        0: "Low Risk",
        1: "Medium Risk",
        2: "High Risk"
    }
    return risk_mapping.get(prediction, "Unknown Risk")
