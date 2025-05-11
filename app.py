# import streamlit as st
# import pandas as pd
# from model import predict_risk
# from utils import collect_user_input

# # Set up page configuration
# st.set_page_config(
#     page_title="Sistem Prediksi Risiko Kesehatan",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # Sidebar navigation
# st.sidebar.title("Navigasi")
# page = st.sidebar.radio("Pilih Halaman", ["Beranda", "Prediksi"])

# # Page: Beranda
# if page == "Beranda":
#     st.title("Selamat Datang di Sistem Prediksi Risiko Kesehatan")
#     st.write(
#         """
#         Sistem ini dirancang untuk membantu Anda memprediksi risiko kesehatan berdasarkan data yang Anda masukkan.
#         Gunakan navigasi di sidebar untuk berpindah ke halaman prediksi.
#         """
#     )

# # Page: Prediksi
# elif page == "Prediksi":
#     st.title("Dashboard Prediksi Risiko Kesehatan")
#     st.header("Masukan Data Kesehatan Anda")

#     # Collect user input
#     input_df = collect_user_input()

#     # Predict risk
#     if st.button("Prediksi Risiko Kesehatan"):
#         risk = predict_risk(input_df)
#         st.success(f"Risiko Kesehatan Anda adalah: **{risk}**")

import streamlit as st
from utils import collect_user_input
from model import predict_risk

st.set_page_config(page_title="Health Risk Predictor", layout="centered")
st.title("🧠 Health Risk Prediction using MLP")

st.markdown("Isi data berikut untuk memprediksi **Health Risk Level**:")

# Ambil input dari user
user_input_df = collect_user_input()

# Tampilkan data input user (opsional)
with st.expander("Lihat Data Input"):
    st.dataframe(user_input_df)

# Tombol untuk prediksi
if st.button("Prediksi Risiko"):
    prediction_result = predict_risk(user_input_df)
    st.success(f"Hasil Prediksi: **{prediction_result}**")
