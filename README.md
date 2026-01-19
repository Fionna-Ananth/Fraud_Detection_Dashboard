# Fraud Detection Dashboard

This project was developed as part of my **internship at Amdox Technologies**.

## 📌 Project Overview
A **Transaction Monitoring & Fraud Analytics Dashboard** built using **unsupervised machine learning** to identify potentially fraudulent transactions without relying on labeled fraud data.

The system detects anomalies in transaction behavior and presents insights through an interactive dashboard for risk analysis and decision support.

---

## 🔍 Key Features
- Unsupervised fraud detection using **Isolation Forest**
- Real-time transaction monitoring
- Fraud analysis by:
  - Time
  - Transaction amount
  - Location / branch
  - Transaction type
  - Unusual login behavior
- KPI-based fraud insights
- Interactive dashboard built with **Streamlit**

---

## 🧠 Machine Learning Approach
- Algorithm: **Isolation Forest**
- Learning type: **Unsupervised**
- Assumed fraud contamination: ~1%
- Output: Transactions flagged as **Fraud (1)** or **Genuine (0)**

This approach is suitable for real-world fraud scenarios where labeled fraud data is limited or unavailable.

---

## 🛠️ Tech Stack
- Python
- Pandas
- NumPy
- Scikit-learn
- Plotly
- Streamlit

---

## ▶️ How to Run the Project
```bash
pip install streamlit pandas numpy scikit-learn plotly
streamlit run dashboard.py

