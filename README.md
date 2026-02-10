# Customer Churn Prediction – ML + Business Intelligence

This project focuses on predicting customer churn for subscription-based digital services using machine learning and converting predictions into business-ready decisions via an interactive Streamlit dashboard.

Instead of stopping at model accuracy, the project emphasizes how churn models are actually used in companies — by combining ML probabilities with business rules to support retention strategies.

---

## Project Motivation

Customer churn is a major revenue challenge for subscription businesses.
The goal of this project is to:

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
Machine Learning & Data Analytics Project
