import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Predicción de precios de automóviles",
    page_icon="🚗"
)

st.title("🚗 Predicción de precios de automóviles")

# Cargar modelo (con cache para que no se recargue siempre)
@st.cache_resource
def load_model():
    return joblib.load("model.joblib")

try:
    model = load_model()
except Exception as e:
    st.error("❌ Error al cargar el modelo")
    st.exception(e)
    st.stop()

st.success("✅ Modelo cargado correctamente")

st.write("Ingresa las características del automóvil:")

# FORMULARIO (ajustado a tus columnas reales)
with st.form("car_form"):
    prod_year = st.number_input("Año de producción", min_value=1980, max_value=2025, value=2015)
    engine_volume = st.number_input("Engine volume", min_value=0.5, max_value=10.0, value=2.0, step=0.1)
    mileage = st.number_input("Kilometraje", min_value=0, max_value=500000, value=80000)
    cylinders = st.number_input("Cilindros", min_value=1, max_value=12, value=4)

    submitted = st.form_submit_button("Predecir precio")

if submitted:
    input_df = pd.DataFrame([{
        "ID": 0,
        "Levy": 0,
        "Manufacturer": "Unknown",
        "Model": "Unknown",
        "Prod. year": prod_year,
        "Category": "Unknown",
        "Leather interior": "No",
        "Fuel type": "Petrol",
        "Engine volume": engine_volume,
        "Mileage": mileage,
        "Cylinders": cylinders,
        "Gear box type": "Automatic",
        "Drive wheels": "Front",
        "Doors": "04-May",
        "Wheel": "Left wheel",
        "Color": "Black",
        "Airbags": 2
    }])
    try:
        prediction = model.predict(input_df)[0]
        st.success(f"💰 Precio estimado: {prediction:,.2f}")
    except Exception as e:
        st.error("❌ Error al hacer la predicción")
        st.exception(e)










