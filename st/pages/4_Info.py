import streamlit as st

st.set_page_config(page_title="Employee Insights", layout="wide")

st.markdown("""
## 📄 Project Summary

---

### 🔹 Page 1: **Attrition Prediction**
- **Purpose**: Predict whether an employee will leave the company or not.
- **Inputs**:
  - BusinessTravel
  - Department
  - EducationField
  - Gender
  - JobRole
  - MonthlyIncome
  - OverTime
  - PercentSalaryHike
  - PerformanceRating
  - TotalWorkingYears
  - YearsSinceLastPromotion
- **Encoding**:
  - Label Encoding for binary columns (e.g., Gender, OverTime)
  - One-Hot Encoding for categorical features (e.g., Department, JobRole)
- **Model**: `v2_Attr_rf_mdl_1.pkl`
- **Output**: Shows whether the employee is likely to leave or stay.

---

### 🔹 Page 2: **Performance Rating Prediction**
- **Purpose**: Predict employee performance rating ( 3 or 4)
- **Inputs**:
  - Age
  - BusinessTravel
  - Education
  - JobInvolvement
  - JobSatisfaction
  - MonthlyIncome
  - PercentSalaryHike
  - YearsAtCompany
  - YearsInCurrentRole
  - YearsSinceLastPromotion
- **Preprocessing**:
  - StandardScaler is used to scale the numerical input
- **Model**: `v3_emp_perf_mdl_2.pkl`
- **Output**: Predicted performance rating (3 or 4)

---
""")

st.markdown("""
⚠️ **Disclaimer:**  
This model has been trained for educational purposes only.  
It may not always provide accurate predictions and should not be used for real-world decision-making.
""")

