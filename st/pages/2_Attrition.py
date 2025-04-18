import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("C:/Users/ragu/Mini_pj_4/Streamlet UI/Model/v2_Attr_rf_mdl_1.pkl")

st.set_page_config(page_title="Attrition Predictor", layout="centered")

st.title("👨‍💼 Employee Attrition Predictor")
st.write("Fill in the employee details below to predict attrition likelihood.")

# Dropdown mappings
bt_map = {"Non-Travel": 0, "Travel_Rarely": 1, "Travel_Frequently": 2}
dept_map = {"Human Resources": 1, "Research & Development": 2, "Sales": 3}
edu_map = {"Human Resources": 1, "Marketing": 2, "Medical": 3, "Life Sciences": 4, "Technical Degree": 5, "Other": 6}
gender_map = {"Female": 0, "Male": 1}
ot_map = {"No": 0, "Yes": 1}
jr_map = {
    "Sales Executive": 1,
    "Research Scientist": 2,
    "Laboratory Technician": 3,
    "Manager": 4,
    "Sales Representative": 5,
    "Healthcare Representative": 6,
    "Human Resources": 7,
    "Manufacturing Director": 8,
    "Research Director": 9
}

# Collect user input
with st.form("attrition_form"):
    col1, col2 = st.columns(2)

    with col1:
        bt = st.selectbox("Business Travel", list(bt_map.keys()))
        dept = st.selectbox("Department", list(dept_map.keys()))
        edu = st.selectbox("Education Field", list(edu_map.keys()))
        jr = st.selectbox("Job Role", list(jr_map.keys()))
        gender = st.selectbox("Gender", list(gender_map.keys()))
        ot = st.selectbox("OverTime", list(ot_map.keys()))

    with col2:
        income = st.number_input("Monthly Income", min_value=1000, max_value=100000, value=5000)
        hike = st.slider("Percent Salary Hike", 0, 100, 15)
        rating = st.slider("Performance Rating", 1, 4, 3)
        years = st.slider("Total Working Years", 0, 40, 10)
        promo = st.slider("Years Since Last Promotion", 0, 20, 1)

    submitted = st.form_submit_button("Predict Attrition")

# Function to encode and align
def prepare_input():
    input_dict = {
        'MonthlyIncome': income,
        'OverTime': ot_map[ot],
        'Gender': gender_map[gender],
        'PercentSalaryHike': hike,
        'PerformanceRating': rating,
        'TotalWorkingYears': years,
        'YearsSinceLastPromotion': promo
    }

    df = pd.DataFrame([input_dict])

    # One-hot encode categorical features
    def one_hot(df, val, prefix, mapping):
        for k, v in mapping.items():
            df[f"{prefix}_{v}"] = 1 if val == k else 0

    one_hot(df, bt_map[bt], 'BusinessTravel', {1: 'Travel_Rarely', 2: 'Travel_Frequently'})
    one_hot(df, dept_map[dept], 'Department', {1: 'Human Resources', 2: 'Research & Development', 3: 'Sales'})
    one_hot(df, edu_map[edu], 'EducationField', {
        1: 'Human Resources', 2: 'Marketing', 3: 'Medical', 4: 'Life Sciences',
        5: 'Technical Degree', 6: 'Other'
    })
    one_hot(df, jr_map[jr], 'JobRole', {
        1: 'Sales Executive', 2: 'Research Scientist', 3: 'Laboratory Technician',
        4: 'Manager', 5: 'Sales Representative', 6: 'Healthcare Representative',
        7: 'Human Resources', 8: 'Manufacturing Director', 9: 'Research Director'
    })

    # Align with model input
    model_features = model.feature_names_in_
    for col in model_features:
        if col not in df.columns:
            df[col] = 0
    df = df[model_features]
    return df

# Predict
if submitted:
    final_input = prepare_input()
    prediction = model.predict(final_input)[0]
    result = "🔥 Yes (High Attrition Risk)" if prediction == 1 else "✅ No (Likely to Stay)"
    st.success(f"Prediction: {result}")
