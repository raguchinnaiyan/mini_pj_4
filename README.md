# mini_pj_4

A Streamlit-based web app that predicts employee attrition and also their performance rating using a machine learning model. It helps HR teams identify potential employee exits based on features like job role, satisfaction, income, and work-life balance. Built with Python, scikit-learn, and joblib. Clone the repo, install dependencies from `requirements.txt`, and run the app using `streamlit run st/1_Home.py`. Visual UI, real-time predictions, and user-friendly design included. Ideal for HR analytics and decision support.

```
mini_pj_4/
│
├── st/                                # 📦 Main app folder
│   ├── 1_Home.py                      # 🏠 Home page with app overview & navigation
│
│   ├── Images/                        # 🖼️ Folder for UI visuals
│   │   └── employee-attrition.png     # - Used on home screen for design
│
│   ├── Model/                         # 🤖 Pre-trained ML models
│   │   ├── v2_Attr_rf_mdl_1.pkl       # - Model for Employee Attrition Prediction
│   │   └── v3_emp_perf_mdl_2          # - Model for Employee Performance Prediction
│
│   └── pages/                         # 📄 Sub-pages (auto-loaded by Streamlit)
│       ├── 2_Attrition.py             # - Page for Employee Attrition Prediction
│       └── 3_Performance.py           # - Page for Employee Performance Prediction
│
├── requirements.txt                   # 📦 Python package dependencies
├── README.md                          # 📘 Project description and setup guide
```
