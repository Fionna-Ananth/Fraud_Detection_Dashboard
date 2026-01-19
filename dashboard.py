import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Fraud Detection Dashboard", layout="wide")

# Load data
df = pd.read_csv("unsupervised_fraud_results.csv")

st.title("Transaction Monitoring & Fraud Analytics Dashboard")
st.subheader("Real-Time Risk Insights using Machine Learning")

# Sidebar navigation
st.sidebar.title("📊 Pages")
page = st.sidebar.radio(
    "Select Page",
    [
        "1. Overview",
        
        "2. Time Analysis",
        "3. Transaction Type",
        "4. Location Analysis",
        "5. Amount Analysis",
        "6. Unusual Login",
        "7. Fraud Deep Dive",
        "8. KPI Metrics",
        "9. Comparative Analysis",
        "10. Conclusion"
    ]
)

# ---------------- PAGE 1 ----------------
if page == "1. Overview":
    st.title(" Overview")

    c1, c2, c3 = st.columns(3)
    c1.metric("Total Transactions", len(df))
    c2.metric("Fraud Cases", df["Anomaly"].sum())
    c3.metric("Fraud %", f"{df['Anomaly'].mean()*100:.2f}")

    st.plotly_chart(px.pie(df, names="Anomaly", title="Fraud vs Genuine"), use_container_width=True)
    st.plotly_chart(px.histogram(df, x="amount", title="Transaction Amount Distribution"),
                     use_container_width=True)

# ---------------- PAGE 2 ----------------
elif page == "2. Time Analysis":
    st.title(" Time-Based Analysis")

    st.plotly_chart(px.histogram(df, x="Time of day", color="Anomaly",
                                 title="Fraud by Time of Day"),
                     use_container_width=True)

    st.plotly_chart(px.histogram(df, x="DayOfWeek", color="Anomaly",
                                 title="Fraud by Day of Week"),
                     use_container_width=True)

    st.plotly_chart(px.line(df.groupby("DayOfWeek")["Anomaly"].mean().reset_index(),
                            x="DayOfWeek", y="Anomaly",
                            title="Average Fraud Trend"),
                     use_container_width=True)

# ---------------- PAGE 3 ----------------
elif page == "3. Transaction Type":
    st.title(" Transaction Type Analysis")

    st.plotly_chart(px.bar(df.groupby("type")["Anomaly"].sum().reset_index(),
                           x="type", y="Anomaly",
                           title="Fraud by Transaction Type"),
                     use_container_width=True)

    st.plotly_chart(px.pie(df, names="type", title="Transaction Type Share"),
                     use_container_width=True)

    st.dataframe(df.groupby("type")["Anomaly"].mean()
                 .reset_index().rename(columns={"Anomaly": "Fraud Ratio"}))

# ---------------- PAGE 4 ----------------
elif page == "4. Location Analysis":
    st.title(" Location Analysis")

    st.plotly_chart(px.bar(
        df.groupby("branch")["Anomaly"].sum().reset_index().sort_values("Anomaly", ascending=False).head(10),
        x="branch", y="Anomaly",
        title="Top Fraud-Prone Branches"),
        use_container_width=True)

    st.plotly_chart(px.pie(df, names="branch", title="Transaction Share by Branch"),
                     use_container_width=True)

    st.metric("Highest Fraud Branch",
              df.groupby("branch")["Anomaly"].sum().idxmax())

# ---------------- PAGE 5 ----------------
elif page == "5. Amount Analysis":
    st.title(" Amount-Based Analysis")

    st.plotly_chart(px.histogram(df, x="amount", nbins=40,
                                 title="Amount Distribution"),
                     use_container_width=True)

    st.plotly_chart(px.box(df, x="Anomaly", y="amount",
                           title="Fraud vs Amount"),
                     use_container_width=True)

    st.metric("Max Fraud Amount",
              df[df["Anomaly"] == 1]["amount"].max())

# ---------------- PAGE 6 ----------------
elif page == "6. Unusual Login":
    st.title(" Unusual Login Analysis")

    st.plotly_chart(px.bar(
        df.groupby("unusuallogin")["Anomaly"].sum().reset_index(),
        x="unusuallogin", y="Anomaly",
        title="Fraud vs Unusual Login"),
        use_container_width=True)

    st.plotly_chart(px.pie(df, names="unusuallogin",
                           title="Login Type Distribution"),
                     use_container_width=True)

    st.metric("Fraud with Unusual Login",
              df[df["unusuallogin"] == 1]["Anomaly"].sum())

# ---------------- PAGE 7 ----------------
elif page == "7. Fraud Deep Dive":
    st.title(" Fraud Deep Dive")

    frauds = df[df["Anomaly"] == 1]

    st.metric("Total Fraud Transactions", len(frauds))
    st.metric("Average Fraud Amount", frauds["amount"].mean())

    st.plotly_chart(px.histogram(frauds, x="amount",
                                 title="Fraud Amount Distribution"),
                     use_container_width=True)

    st.dataframe(frauds.head(20))

# ---------------- PAGE 8 ----------------
elif page == "8. KPI Metrics":
    st.title(" Key Performance Indicators")

    c1, c2, c3 = st.columns(3)
    c1.metric("Fraud %", f"{df['Anomaly'].mean()*100:.2f}")
    c2.metric("Highest Amount", df["amount"].max())
    c3.metric("Avg Fraud Amount", df[df["Anomaly"] == 1]["amount"].mean())

    st.plotly_chart(px.bar(
        df.groupby("branch")["Anomaly"].mean().reset_index(),
        x="branch", y="Anomaly",
        title="Fraud Ratio by Branch"),
        use_container_width=True)

# ---------------- PAGE 9 ----------------
elif page == "9. Comparative Analysis":
    st.title(" Comparative Analysis")

    st.plotly_chart(px.histogram(df, x="amount", color="Anomaly",
                                 title="Fraud vs Genuine Amount"),
                     use_container_width=True)

    st.plotly_chart(px.box(df, x="type", y="amount", color="Anomaly",
                           title="Transaction Type Comparison"),
                     use_container_width=True)

    st.plotly_chart(px.bar(df.groupby("type")["Anomaly"].mean().reset_index(),
                           x="type", y="Anomaly",
                           title="Fraud Ratio Comparison"),
                     use_container_width=True)

# ---------------- PAGE 10 ----------------
elif page == "10. Conclusion":
    st.title(" Conclusion")

    st.metric("Total Transactions", len(df))
    st.metric("Fraud Detected", df["Anomaly"].sum())
    st.metric("Fraud %", f"{df['Anomaly'].mean()*100:.2f}%")
