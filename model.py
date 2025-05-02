import joblib
import pandas as pd

def load_model():
  model = joblib.load("./model/model_rf.pkl")
  return model 

def predict_risk(input_data):
  model = load_model()
  prediction = model.predict(input_data)
  return prediction[0]