import streamlit as st
import numpy as np
import pandas as pd
import pickle

# ── Load Models ───────────────────────────────────
ridge_model = pickle.load(open("models/ridge.pkl", "rb"))
scaler_model = pickle.load(open("models/scaler.pkl", "rb"))

# ── UI ────────────────────────────────────────────
st.set_page_config(page_title="🔥 Forest Fire Prediction", layout="centered")

st.title("🔥 Algerian Forest Fire Prediction")

st.markdown("Enter the values below:")

# Inputs
temperature = st.number_input("Temperature")
rh = st.number_input("RH")
ws = st.number_input("Wind Speed")
rain = st.number_input("Rain")

ffmc = st.number_input("FFMC")
dmc = st.number_input("DMC")
isi = st.number_input("ISI")
classes = st.number_input("Classes (0 or 1)")
region = st.number_input("Region (0 or 1)")

# ── Prediction ────────────────────────────────────
if st.button("Predict"):

    data = pd.DataFrame(
        [[temperature, rh, ws, rain, ffmc, dmc, isi, classes, region]],
        columns=[
            "Temperature",
            "RH",
            "Ws",
            "Rain",
            "FFMC",
            "DMC",
            "ISI",
            "Classes",
            "Region",
        ],
    )

    scaled_data = scaler_model.transform(data)
    prediction = ridge_model.predict(scaled_data)[0]

    # Risk logic
    if prediction < 10:
        risk = "Low 🟢"
    elif prediction < 30:
        risk = "Moderate 🟡"
    elif prediction < 60:
        risk = "High 🟠"
    else:
        risk = "Extreme 🔴"

    # Output
    st.subheader("Result")
    st.write(f"FWI: {prediction:.2f}")
    st.write(f"Risk Level: {risk}")

    st.dataframe(data)