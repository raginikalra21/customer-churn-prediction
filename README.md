<<<<<<< HEAD
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
=======
# Customer Churn Prediction – ML + Business Intelligence
>>>>>>> fe6bcbc (Update README with concise project overview and business context)

This project focuses on predicting customer churn for subscription-based digital services using machine learning and converting predictions into business-ready decisions via an interactive Streamlit dashboard.

<<<<<<< HEAD
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
=======
Instead of stopping at model accuracy, the project emphasizes how churn models are actually used in companies — by combining ML probabilities with business rules to support retention strategies.
>>>>>>> fe6bcbc (Update README with concise project overview and business context)

---

<<<<<<< HEAD
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
=======
## Project Motivation

Customer churn is a major revenue challenge for subscription businesses.
The goal of this project is to:
>>>>>>> fe6bcbc (Update README with concise project overview and business context)

- Identify customers likely to churn
- Understand key churn drivers
- Present results in a usable decision system, not just notebooks

This project was inspired by the IBM Watson Analytics churn use case.

---

## Dataset

- Telco Customer Churn dataset
- ~7,000 customer records
- Binary target variable: Churn (Yes / No)

### Feature Groups

- Customer tenure and contract details
- Billing and payment methods
- Internet and service subscriptions
- Customer support and security services

---

## Approach

### 1. Exploratory Data Analysis
- Churn distribution analysis
- Contract type vs churn
- Tenure vs churn trends
- Identification of high-impact features

### 2. Data Preprocessing
- Missing value handling (TotalCharges)
- Encoding categorical variables
- Feature scaling
- Handling class imbalance

### 3. Feature Engineering
- Average monthly spend
- High-tenure indicator
- Contract and service-based flags

---

## Models Used

- Logistic Regression (baseline)
- Random Forest
- XGBoost (final model)

XGBoost was selected for its ability to capture non-linear relationships and interactions between customer behavior and service usage.

---

## Model Evaluation

Evaluation focused on metrics relevant to churn problems:

- Accuracy
- Precision
- Recall (priority)
- F1-Score
- ROC-AUC
- Confusion Matrix

Recall was prioritized since failing to identify a churned customer is more costly than a false positive.

---

## Why Probabilities Look Conservative

The model outputs calibrated churn probabilities, which tend to be conservative by design.

In real churn systems:
- Even 10–25% churn probability is considered risky
- Decisions are rarely made using raw probabilities alone

To address this, a business risk layer was added.

---

## Business Risk Layer

A rule-based risk adjustment is applied on top of the ML probability using factors such as:

- Very low tenure
- Month-to-month contracts
- Lack of tech support or online security
- Paperless billing

This converts model outputs into actionable churn risk levels, similar to real production systems.

---

## Streamlit Dashboard

The project includes a production-style Streamlit application with:

- Clean, enterprise-style UI
- KPI summary cards
- Dataset-aligned input controls
- Auto-computed lifetime value
- Business-adjusted churn risk classification

### Risk Levels
- Low Risk
- Moderate Risk
- High Risk

---

## Project Structure

customer-churn-prediction/
│
├── app.py                  # Streamlit application
├── models/
│   ├── churn_model.pkl     # Trained XGBoost model
│   └── scaler.pkl          # Feature scaler
│
├── notebooks/
│   ├── eda.ipynb
│   └── model_training.ipynb
│
├── data/
│   └── raw/
│
├── requirements.txt
└── README.md

---

## How to Run

pip install -r requirements.txt
streamlit run app.py

<<<<<<< HEAD
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
=======
---

## Key Takeaways

- Churn is driven more by service experience than price alone
- Calibrated ML models require business interpretation
- Deployment quality matters as much as model accuracy

---

## Future Improvements

- SHAP-based feature explainability
- Customer-specific churn explanations
- Retention strategy recommendations
- Cloud deployment

---

## Author

Ragini Kalra  
>>>>>>> fe6bcbc (Update README with concise project overview and business context)
Machine Learning & Data Analytics Project
