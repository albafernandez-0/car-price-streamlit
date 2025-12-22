import streamlit as st
st.write("✅ app.py se está ejecutando")
st.stop()


import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Predicción de precios de autos", page_icon="🚗")

@st.cache_resource
def load_model():
    return joblib.load("model.pkl")

model = load_model()



