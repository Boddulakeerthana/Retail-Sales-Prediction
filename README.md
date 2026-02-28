# 🛒 Retail Sales Prediction using Machine Learning

## 📌 Project Overview

Retail businesses generate large volumes of transactional data every day. Predicting future sales helps organizations improve inventory planning, pricing strategies, and business decision-making.

This project builds a **Machine Learning model** to predict **Retail Sales Amount** based on customer demographics, product category, and purchase details. The trained model is deployed using **Streamlit** as an interactive web application.

---

## 🚀 Live Application

👉 Live Demo:  
https://retail-sales-prediction-k73fav9ndrbuchmgdapkx9.streamlit.app/

---

## 🎯 Problem Statement

Predict the **Total Sales Amount** of a retail transaction using historical data.

The model learns relationships between:
- Customer information
- Product category
- Purchase quantity
- Price details
- Date-based features

---

## 🧠 Machine Learning Workflow

1. Data Collection
2. Data Preprocessing
3. Feature Engineering
4. Exploratory Data Analysis (EDA)
5. Model Training
6. Model Evaluation
7. Model Comparison
8. Deployment using Streamlit

---

## 📂 Dataset Features

| Feature | Description |
|--------|-------------|
| Age | Customer age |
| Gender | Male / Female |
| Product Category | Beauty / Clothing / Electronics |
| Quantity | Number of items |
| Price per Unit | Product price |
| Year | Purchase year |
| Month | Purchase month |
| Day | Purchase day |
| Weekday | Day of week |
| Total Amount | Target variable |

---

## ⚙️ Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Joblib
- Git & GitHub

---

## 📊 Models Implemented

### 1️⃣ Linear Regression
- Used as baseline model
- Captures linear relationships

### 2️⃣ Random Forest Regressor (Final Model ✅)
- Ensemble learning algorithm
- Handles nonlinear patterns
- Provides better prediction performance

---

## 📈 Evaluation Metrics

Models evaluated using:

- **R² Score**
- **RMSE (Root Mean Squared Error)**
- **MAE (Mean Absolute Error)**

Random Forest outperformed Linear Regression.

---

## 🖥️ Streamlit Web Application

Users can:

✅ Enter customer details  
✅ Select product category  
✅ Provide purchase information  
✅ Get instant sales prediction

## 🌐 Deployment

The application is deployed using Streamlit Community Cloud.

## 💡 Key Learnings

End-to-end Machine Learning pipeline
Feature engineering
Model evaluation & comparison
Model deployment using Streamlit
Real-world ML application building

## 🔮 Future Enhancements

Add XGBoost / Gradient Boosting
Dashboard visualization
API deployment using FastAPI
Real-time sales analytics

