import joblib
import pandas as pd

def load_model():
    model = joblib.load("./model/model_rf.pkl")
    return model 

def predict_risk(input_data):
    model = load_model()
    print("Input Data:", input_data)  # Debug: Print input data
    prediction = model.predict(input_data)[0]
    print("Raw Prediction:", prediction)  # Debug: Print raw prediction
    risk_mapping = {
        0: "Low Risk",
        1: "Medium Risk",
        2: "High Risk"
    }
    return risk_mapping.get(prediction, "Unknown Risk")