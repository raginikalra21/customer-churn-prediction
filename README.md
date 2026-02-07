📊 Customer Churn Prediction – Churn Intelligence Platform
An end-to-end machine learning project that predicts customer churn in subscription-based digital services and converts model outputs into business-ready churn risk decisions using a production-style Streamlit dashboard.
This project goes beyond a basic ML prototype by combining:
Calibrated ML probabilities
Business risk rules
Enterprise-grade UI

🚀 Project Overview
Customer churn directly impacts revenue in subscription businesses.
This project builds a classification-based churn prediction system that helps businesses identify high-risk customers early and take proactive retention actions.
The solution follows a real industry workflow:
EDA → Feature Engineering → Model Training → Evaluation → Business Logic → Deployment

🎯 Objectives
Predict whether a customer is likely to churn
Prioritize Recall & ROC-AUC for churn detection
Translate ML outputs into actionable business risk
Deploy a company-ready dashboard, not just a notebook

🗂 Dataset
Source: Telco Customer Churn Dataset
Rows: ~7,000 customers
Target Variable: Churn (Yes / No)
Feature Categories
Customer tenure & contract details
Billing & payment information
Internet & service subscriptions
Support & security services

🧠 Methodology
1️⃣ Exploratory Data Analysis (EDA)
Churn distribution analysis
Contract type vs churn
Tenure vs churn behavior
Identification of key churn drivers
2️⃣ Data Preprocessing
Handling missing values (TotalCharges)
Encoding categorical variables
Feature scaling
Handling class imbalance
3️⃣ Feature Engineering
Average monthly charge
High-tenure indicator
Contract & service indicators

🤖 Models Trained
Model	Purpose
Logistic Regression	Baseline
Random Forest	Non-linear patterns
XGBoost	Final production model

📊 Model Evaluation
Key metrics used:
Accuracy
Precision
Recall (priority metric)
F1-Score
ROC-AUC
Confusion Matrix
In churn prediction, missing a churned customer is more costly than a false alarm, hence Recall is emphasized.

🧠 Why Probabilities Look “Low”
The model outputs calibrated churn probabilities, which are intentionally conservative.
A churn probability of 15–25% is already significant
Production systems rarely act on raw probabilities alone

🧩 Business Risk Layer (Key Innovation)
To make predictions actionable, a business decision layer is added on top of the ML model.
Business Risk Factors
Very low tenure
Month-to-month contract
Lack of tech support or online security
Paperless billing
High price sensitivity

Final Decision Logic
Final Risk Score = Model Probability + Business Risk Adjustments
This mirrors how real companies deploy churn models.

🖥 Streamlit Dashboard (Enterprise-Style)
The project includes a production-ready Streamlit app:
Features
Clean, enterprise UI
KPI cards & structured layout
Dataset-aligned inputs
Service & support risk toggles
Business-level churn risk classification

Risk Categories
🟢 Baseline Risk
🟠 Moderate Risk
🔴 High Risk

📁 Project Structure
customer-churn-prediction/
│
├── app.py                  # Streamlit dashboard
├── models/
│   ├── churn_model.pkl     # Trained XGBoost model
│   └── scaler.pkl          # Feature scaler
│
├── notebooks/
│   ├── 01_eda.ipynb
│   └── 02_model_training.ipynb
│
├── data/
│   └── raw/
│
├── requirements.txt
└── README.md


▶️ How to Run the Project
1️⃣ Install Dependencies
pip install -r requirements.txt
2️⃣ Run the Dashboard
streamlit run app.py

🧪 Example High-Risk Scenario
Tenure: 1 month
Contract: Month-to-month
Monthly Charges: High
Tech Support: No
Online Security: No
➡️ High churn risk flagged with actionable recommendations

📌 Key Learnings
Churn is driven more by behavior & service experience than price alone
Calibrated ML models need a business decision layer
Deployment quality matters as much as model accuracy

🔮 Future Enhancements
SHAP-based explainability
Customer-level churn explanations
Automated retention strategy recommendations
Cloud deployment (Streamlit Cloud / AWS)

🏁 Final Note
This project is built to reflect real-world ML systems, not just academic prototypes.
“Model probability + business logic = production-grade decision system.”

👤 Author
Ragini Kalra
Machine Learning & Data Analytics Project
