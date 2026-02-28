import streamlit as st
import numpy as np
import joblib

# -----------------------------
# Load trained model
# -----------------------------
model = joblib.load("retail_model.pkl")

# -----------------------------
# App Title
# -----------------------------
st.title("🛒 Retail Sales Prediction App")
st.write("Enter customer and product details to predict sales.")

# -----------------------------
# User Inputs
# -----------------------------
age = st.number_input("Age", min_value=18, max_value=70, value=25)
quantity = st.number_input("Quantity", min_value=1, max_value=10, value=1)
price = st.number_input("Price per Unit", min_value=1, max_value=1000, value=100)

gender = st.selectbox("Gender", ["Female", "Male"])

category = st.selectbox(
    "Product Category",
    ["Beauty", "Clothing", "Electronics"]
)

year = st.number_input("Year", min_value=2020, max_value=2030, value=2023)
month = st.slider("Month", 1, 12, 1)
day = st.slider("Day", 1, 31, 1)
weekday = st.slider("Weekday (0=Mon, 6=Sun)", 0, 6, 0)

# -----------------------------
# Encoding (MUST match training)
# -----------------------------
gender_male = 1 if gender == "Male" else 0
cat_clothing = 1 if category == "Clothing" else 0
cat_electronics = 1 if category == "Electronics" else 0

# -----------------------------
# Prediction Button
# -----------------------------
if st.button("Predict Sales"):

    # IMPORTANT: feature order SAME as notebook training
    features = np.array([[
        age,
        quantity,
        price,
        year,
        month,
        day,
        weekday,
        gender_male,
        cat_clothing,
        cat_electronics
    ]])

    prediction = model.predict(features)

    st.success(f"💰 Predicted Sales Amount: ₹ {prediction[0]:.2f}")
