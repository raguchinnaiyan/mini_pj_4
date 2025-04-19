import streamlit as st
from PIL import Image

# App title
st.set_page_config(page_title="Employee Insights", layout="wide")


st.title("👨‍💼 Employee Insights Dashboard")
st.subheader("Predict Attrition & Evaluate Performance")

# Description
st.markdown("""
Welcome to the **Employee Insights Dashboard**. This application is designed to help HR professionals and managers gain data-driven insights into:

- **Employee Attrition**: Predict the likelihood of an employee leaving the organization.
- **Employee Performance**: Analyze and forecast employee performance based on historical data.

Use the sidebar to navigate between the two models.
""")

# Two-column layout for features
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🔄 Employee Attrition Prediction")
    st.image("st/Images/employee-attrition.png", width=650)
    st.markdown("""
    - Predict if an employee is at risk of leaving.
    - Explore key factors like job role, satisfaction, salary, and more.
    - Use classification models trained on HR data.
    """)

with col2:
    st.markdown("### 📈 Performance Evaluation")
    st.image("st/Images/employee-performance.png", width=310)
    st.markdown("""
    - Evaluate employee performance levels.
    - Understand contributors to high and low performance.
    - Based on metrics such as projects, experience, and ratings.
    """)

st.markdown("---")
st.markdown("🔍 **Tip**: Navigate using the sidebar to try out the models!")
