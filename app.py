import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("retail_model.pkl", "rb"))

st.title("🛒 Retail Sales Prediction App")
st.write("Enter customer and product details to predict sales.")

# Inputs
age = st.number_input("Age", 18, 70)
quantity = st.number_input("Quantity", 1, 10)
price = st.number_input("Price per Unit", 1, 1000)

gender = st.selectbox("Gender", ["Female", "Male"])
category = st.selectbox(
    "Product Category",
    ["Beauty", "Clothing", "Electronics"]
)
year = st.number_input("Year", 2020, 2030, value=2023)
month = st.slider("Month", 1, 12)
day = st.slider("Day", 1, 31)
weekday = st.slider("Weekday (0=Mon,6=Sun)", 0, 6)

# Encoding
gender_male = 1 if gender == "Male" else 0
cat_clothing = 1 if category == "Clothing" else 0
cat_electronics = 1 if category == "Electronics" else 0

# Prediction
if st.button("Predict Sales"):

    features = np.array([[age,
                      quantity,
                      price,
                      year,
                      month,
                      day,
                      weekday,
                      gender_male,
                      cat_clothing,
                      cat_electronics]])

    prediction = model.predict(features)

    st.success(f"Predicted Sales Amount: ₹ {prediction[0]:.2f}")