import random

def predict_risk(df):
    # Dummy logic (replace with model.predict)
    risk_levels = ["Low", "Moderate", "High"]
    return random.choices(risk_levels, weights=[0.3, 0.5, 0.2])[0]
