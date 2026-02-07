import streamlit as st
import pandas as pd
import joblib
import os

# ======================================================
# PAGE CONFIG
# ======================================================
st.set_page_config(
    page_title="Churn Intelligence Platform",
    page_icon="📉",
    layout="wide"
)

# ======================================================
# LOAD MODEL & SCALER
# ======================================================
BASE_DIR = os.path.dirname(__file__)
model = joblib.load(os.path.join(BASE_DIR, "models/churn_model.pkl"))
scaler = joblib.load(os.path.join(BASE_DIR, "models/scaler.pkl"))
FEATURES = model.get_booster().feature_names

# ======================================================
# UI STYLING (ENTERPRISE)
# ======================================================
st.markdown("""
<style>
html, body { background-color: #020617; font-family: 'Inter', sans-serif; }
.block-container { padding-top: 2rem; }

.title { font-size: 46px; font-weight: 800; }
.subtitle { color: #94a3b8; margin-bottom: 25px; }

.metric-card {
    background: linear-gradient(145deg, #020617, #0f172a);
    border-radius: 20px;
    padding: 24px;
    color: white;
    box-shadow: 0 18px 45px rgba(0,0,0,0.55);
}

.section {
    background: #020617;
    border-radius: 24px;
    padding: 32px;
    margin-bottom: 35px;
    border: 1px solid #1e293b;
}

.stButton > button {
    width: 100%;
    background: linear-gradient(135deg, #38bdf8, #6366f1);
    color: black;
    font-size: 18px;
    font-weight: 800;
    padding: 16px;
    border-radius: 18px;
}

.footer {
    color: #64748b;
    font-size: 13px;
    text-align: center;
    margin-top: 40px;
}
</style>
""", unsafe_allow_html=True)

# ======================================================
# HEADER
# ======================================================
st.markdown("<div class='title'>📊 Churn Intelligence Platform</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Model probability + business risk intelligence</div>", unsafe_allow_html=True)
st.markdown("---")

# ======================================================
# KPI CARDS
# ======================================================
k1, k2, k3 = st.columns(3)

with k1:
    st.markdown("""
    <div class="metric-card">
        <h4>📉 Objective</h4>
        <h2>Churn Reduction</h2>
        <p>Retention-driven decisions</p>
    </div>
    """, unsafe_allow_html=True)

with k2:
    st.markdown("""
    <div class="metric-card">
        <h4>🧠 Model</h4>
        <h2>XGBoost</h2>
        <p>Calibrated probability</p>
    </div>
    """, unsafe_allow_html=True)

with k3:
    st.markdown("""
    <div class="metric-card">
        <h4>⚡ Decision Layer</h4>
        <h2>Business Rules</h2>
        <p>Actionable risk scoring</p>
    </div>
    """, unsafe_allow_html=True)

# ======================================================
# CUSTOMER PROFILE
# ======================================================
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.subheader("👤 Customer Subscription Profile")

c1, c2, c3 = st.columns(3)

with c1:
    tenure = st.slider("Tenure (months)", 0, 72, 12)
    contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])

with c2:
    monthly_charges = st.slider("Monthly Charges (₹)", 10, 200, 70)
    internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])

with c3:
    payment_method = st.selectbox(
        "Payment Method",
        ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"]
    )

total_charges = tenure * monthly_charges
st.info(f"💰 **Lifetime Value (Auto-Computed): ₹{total_charges:.2f}**")
st.markdown("</div>", unsafe_allow_html=True)

# ======================================================
# SERVICE SIGNALS (DATASET-ALIGNED)
# ======================================================
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.subheader("🛠 Service & Support Signals")

s1, s2, s3 = st.columns(3)

with s1:
    tech_support = st.selectbox("Tech Support", ["Yes", "No"])
    online_security = st.selectbox("Online Security", ["Yes", "No"])

with s2:
    device_protection = st.selectbox("Device Protection", ["Yes", "No"])
    streaming_tv = st.selectbox("Streaming TV", ["Yes", "No"])

with s3:
    paperless_billing = st.selectbox("Paperless Billing", ["Yes", "No"])

st.markdown("</div>", unsafe_allow_html=True)

# ======================================================
# FEATURE ENGINEERING (MODEL INPUT)
# ======================================================
data = {
    "tenure": tenure,
    "MonthlyCharges": monthly_charges,
    "TotalCharges": total_charges,
    "AvgMonthlyCharge": total_charges / (tenure + 1),
    "HighTenure": 1 if tenure > 24 else 0,

    "Contract_One year": 1 if contract == "One year" else 0,
    "Contract_Two year": 1 if contract == "Two year" else 0,

    "InternetService_Fiber optic": 1 if internet_service == "Fiber optic" else 0,
    "InternetService_No": 1 if internet_service == "No" else 0,

    "PaymentMethod_Electronic check": 1 if payment_method == "Electronic check" else 0,
    "PaymentMethod_Mailed check": 1 if payment_method == "Mailed check" else 0,
    "PaymentMethod_Credit card (automatic)": 1 if payment_method == "Credit card (automatic)" else 0,

    "TechSupport_Yes": 1 if tech_support == "Yes" else 0,
    "OnlineSecurity_Yes": 1 if online_security == "Yes" else 0,
    "DeviceProtection_Yes": 1 if device_protection == "Yes" else 0,
    "StreamingTV_Yes": 1 if streaming_tv == "Yes" else 0,
    "PaperlessBilling_Yes": 1 if paperless_billing == "Yes" else 0,
}

input_df = pd.DataFrame([data])
for col in FEATURES:
    if col not in input_df.columns:
        input_df[col] = 0
input_df = input_df[FEATURES]

# ======================================================
# PREDICTION + BUSINESS RISK LAYER  🔥 FIX A
# ======================================================
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.subheader("📈 Churn Risk Assessment")

if st.button("Run AI Risk Analysis"):
    X_scaled = scaler.transform(input_df)
    model_prob = model.predict_proba(X_scaled)[0][1]

    # ---------- BUSINESS RISK LAYER ----------
    risk_score = model_prob

    if tenure < 6:
        risk_score += 0.15
    if contract == "Month-to-month":
        risk_score += 0.15
    if tech_support == "No":
        risk_score += 0.20
    if online_security == "No":
        risk_score += 0.20
    if paperless_billing == "Yes":
        risk_score += 0.05

    risk_score = min(risk_score, 1.0)

    # ---------- DISPLAY ----------
    st.markdown(f"**Model Probability:** {model_prob:.2%}")
    st.markdown(f"**Business Risk Score:** {risk_score:.2%}")

    if risk_score >= 0.65:
        st.error("🚨 **HIGH CHURN RISK — Immediate retention action required**")
    elif risk_score >= 0.40:
        st.warning("⚠️ **MODERATE CHURN RISK — Monitor & engage**")
    else:
        st.success("✅ **BASELINE CHURN RISK — Customer relatively stable**")

st.markdown("</div>", unsafe_allow_html=True)

# ======================================================
# FOOTER
# ======================================================
st.markdown("<div class='footer'>Model probability + business logic = production-grade decision system</div>", unsafe_allow_html=True)
