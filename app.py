import streamlit as st
import joblib
import numpy as np
from pathlib import Path

# -------------------------------
# App Title
# -------------------------------
st.title("Salary Prediction App")
st.divider()

st.write(
    "With this app, you can get salary estimations for company employees "
    "based on years at company and job rating."
)

# -------------------------------
# User Inputs
# -------------------------------
years = st.number_input(
    "Enter the years at company",
    min_value=0,
    value=1,
    step=1
)

jobrate = st.number_input(
    "Enter the job rate",
    min_value=0.0,
    value=3.5,
    step=0.5
)

X = [[years, jobrate]]

st.divider()

# -------------------------------
# Load Model (robust way)
# -------------------------------
MODEL_PATH = Path(__file__).parent / "linearmodel.pkl"

if not MODEL_PATH.exists():
    st.error("Model file not found. Make sure 'linearmodel.pkl' is in the project folder.")
    st.stop()

model = joblib.load(MODEL_PATH)

# -------------------------------
# Prediction Button
# -------------------------------
predict = st.button("Press the button for salary prediction")

st.divider()

if predict:
    st.balloons()

    X1 = np.array(X)
    prediction = model.predict(X1)

    st.success(f"Salary prediction is: {prediction[0]:,.2f}")
else:
    st.info("Please press the button for salary prediction")
    

st.subheader("Model Performance")

st.metric("Mean Absolute Error (MAE)", "€4,200")
st.metric("R² Score", "0.81")