import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler

#Load the trained model
model = joblib.load("C:/Users/ragu/Mini_pj_4/Streamlet UI/Model/v3_emp_perf_mdl_2.pkl")

# scaler 
scaler = joblib.load("C:/Users/ragu/Mini_pj_4/Streamlet UI/Model/scaler.pkl")

#Streamlit UI
st.title("🧠 Employee Performance Rating Predictor")

st.markdown("Please fill in the employee details to predict performance rating.")

#Collect input from user
age = st.number_input("Age", min_value=18, max_value=65, value=30)
business_travel = st.selectbox("Business Travel", [0, 1, 2], format_func=lambda x: ["None", "Rarely", "Frequently"][x])
education = st.slider("Education (1 = Below College, 5 = Doctor)", 1, 5, 3)
job_involvement = st.slider("Job Involvement (1 = Low, 4 = High)", 1, 4, 3)
job_satisfaction = st.slider("Job Satisfaction (1 = Low, 4 = High)", 1, 4, 3)
monthly_income = st.number_input("Monthly Income", min_value=1000, max_value=50000, value=7000)
percent_salary_hike = st.slider("Percent Salary Hike", 0, 100, 15)
years_at_company = st.number_input("Years at Company", min_value=0, max_value=40, value=5)
years_in_current_role = st.number_input("Years in Current Role", min_value=0, max_value=20, value=2)
years_since_last_promotion = st.number_input("Years Since Last Promotion", min_value=0, max_value=20, value=1)

#Create DataFrame from input
input_data = pd.DataFrame([{
    'Age': age,
    'BusinessTravel': business_travel,
    'Education': education,
    'JobInvolvement': job_involvement,
    'JobSatisfaction': job_satisfaction,
    'MonthlyIncome': monthly_income,
    'PercentSalaryHike': percent_salary_hike,
    'YearsAtCompany': years_at_company,
    'YearsInCurrentRole': years_in_current_role,
    'YearsSinceLastPromotion': years_since_last_promotion
}])

#Predict when button is clicked
if st.button("Predict Performance Rating"):
    scaler.fit(input_data)  # Only simulating
    scaled_input = scaler.transform(input_data)

    # Predict
    prediction = model.predict(scaled_input)
    st.success(f"✅ Predicted Performance Rating: {prediction[0]}")