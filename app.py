import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from model import predict_risk
from utils import collect_user_input 

# Set page configuration (must be the first Streamlit command)
st.set_page_config(
    page_title="Sistem Prediksi Risiko Kesehatan",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Add custom CSS for dark theme
st.markdown(
    """
    <style>
    .stApp {
        background-color: #121212;
        color: #E0E0E0;
        font-family: "Arial", sans-serif;
    }
    h1, h2, h3 {
        color: #BB86FC;
    }
    .stButton>button {
        background-color: #BB86FC;
        color: #121212;
        font-size: 16px;
        border-radius: 8px;
        padding: 10px 20px;
    }
    .stButton>button:hover {
        background-color: #3700B3;
    }
    .css-1d391kg {
        background-color: #1E1E1E;
        border-right: 2px solid #BB86FC;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.sidebar.title("Navigasi")
page = st.sidebar.radio("Pilih Halaman", ["Beranda", "Prediksi"])

if page == "Beranda":
    st.title("Sistem Prediksi Risiko Kesehatan")
    st.write(
        """
        Sistem ini dirancang untuk membantu Anda memprediksi risiko kesehatan berdasarkan data yang Anda masukkan.
        Gunakan navigasi di sidebar untuk berpindah ke halaman prediksi.
        """
    )
    
    csv_path = "./data/student_health_data.csv"
    data = pd.read_csv(csv_path, header=None, names=[
        "ID", "Age", "Gender", "Height", "Weight", "HeartRate", "StressLevel", 
        "HappinessLevel", "RiskLevel", "Diet", "MentalState", "BMI", "ActivityLevel", "OverallHealth"
    ])
    
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Distribusi Risiko Kesehatan")
        risk_counts = data["RiskLevel"].value_counts()
        fig1, ax1 = plt.subplots(figsize=(6, 4))
        risk_counts.plot(kind="bar", color=["#BB86FC", "#03DAC6", "#CF6679"], ax=ax1)
        ax1.set_title("Distribusi Risiko Kesehatan")
        ax1.set_xlabel("Risk Level")
        ax1.set_ylabel("Jumlah")
        st.pyplot(fig1)

    with col2:
        st.subheader("Rata-rata Tingkat Stres Berdasarkan Gender")
        data["StressLevel"] = pd.to_numeric(data["StressLevel"], errors="coerce")
        data_cleaned = data.dropna(subset=["StressLevel", "Gender"])
        avg_stress_by_gender = data_cleaned.groupby("Gender")["StressLevel"].mean()
        fig2, ax2 = plt.subplots(figsize=(6, 4))
        avg_stress_by_gender.plot(kind="bar", color=["#BB86FC", "#03DAC6"], ax=ax2)
        ax2.set_title("Rata-rata Tingkat Stres Berdasarkan Gender")
        ax2.set_xlabel("Gender")
        ax2.set_ylabel("Rata-rata Tingkat Stres")
        st.pyplot(fig2)

elif page == "Prediksi":
    st.title("Dashboard Prediksi Risiko Kesehatan")
    st.header("Masukan Data Kesehatan Anda")

    input_df = collect_user_input()

    if st.button("Prediksi Risiko Kesehatan"):
        risk = predict_risk(input_df)
        st.success(f"Risiko Kesehatan Anda adalah: **{risk}**")