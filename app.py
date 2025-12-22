import streamlit as st
import joblib

st.set_page_config(page_title="Predicción de precios de autos", page_icon="🚗")

try:
    model = joblib.load("model.pkl")
except Exception as e:
    st.error("❌ No pude cargar el modelo (model.pkl). Aquí está el error:")
    st.exception(e)
    st.stop()
