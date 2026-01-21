import streamlit as st
import pandas as pd
import json
import os
from openai import OpenAI

# --------------------------------------------------
# Streamlit page config (MUST be first Streamlit call)
# --------------------------------------------------
st.set_page_config(
    page_title="AI Data Quality Assistant",
    layout="wide"
)

# --------------------------------------------------
# App Header
# --------------------------------------------------
st.title("🧹 AI Data Quality & Cleaning Assistant")
st.write(
    "Upload a CSV file to analyze data quality using AI. "
    "Large profiling reports are generated offline for stability."
)

# --------------------------------------------------
# File Upload
# --------------------------------------------------
uploaded_file = st.file_uploader("📤 Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file, encoding="ISO-8859-1")
    except Exception as e:
        st.error(f"❌ Failed to read CSV: {e}")
        st.stop()

    # --------------------------------------------------
    # Dataset Preview
    # --------------------------------------------------
    st.subheader("📄 Dataset Preview")
    st.dataframe(df.head())

    # --------------------------------------------------
    # Lightweight Dataset Summary (Safe for UI + LLM)
    # --------------------------------------------------
    summary = {
        "rows": int(df.shape[0]),
        "columns": int(df.shape[1]),
        "missing_cells": int(df.isna().sum().sum()),
        "missing_percentage": float(df.isna().mean().mean() * 100),
        "duplicate_rows": int(df.duplicated().sum()),
        "dtypes": df.dtypes.astype(str).to_dict(),
    }

    summary_text = json.dumps(summary, indent=2)

    # --------------------------------------------------
    # OpenAI Client (uses secrets.toml or env var)
    # --------------------------------------------------
    client = OpenAI()

    # --------------------------------------------------
    # AI Data Quality Insights
    # --------------------------------------------------
    if st.button("🤖 Generate AI Data Quality Insights"):
        with st.spinner("Analyzing data quality using AI..."):
            prompt = f"""
You are a senior data analyst.

Using the dataset summary below:
1. Identify the most critical data quality issues
2. Explain their business impact
3. Recommend the priority order for cleaning

Dataset Summary:
{summary_text}

Respond in clear bullet points.
"""
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
            )

        st.subheader("🧠 AI Data Quality Insights")
        st.write(response.choices[0].message.content)

    # --------------------------------------------------
    # AI Cleaning Pipeline Generator
    # --------------------------------------------------
    if st.button("🧪 Generate AI Cleaning Code"):
        with st.spinner("Generating AI-powered cleaning pipeline..."):
            cleaning_prompt = f"""
You are a senior data engineer.

Generate production-ready Pandas code to clean this dataset:
- Handle missing values
- Remove duplicates
- Fix incorrect data types
- Handle outliers where applicable

Dataset columns and types:
{df.dtypes}

Rules:
- Use pandas only
- No explanations
- Return only Python code
"""
            cleaning_response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": cleaning_prompt}],
            )

        st.subheader("🧾 AI-Generated Cleaning Pipeline")
        st.code(cleaning_response.choices[0].message.content, language="python")

# --------------------------------------------------
# Offline Profiling Report (Safe & Stable)
# --------------------------------------------------
st.subheader("📊 Data Profiling Report")

st.info(
    "For large datasets, profiling is generated offline to avoid "
    "performance and WebSocket issues."
)

if os.path.exists("online_retail_data_quality_report.html"):
    with open("online_retail_data_quality_report.html", "rb") as f:
        st.download_button(
            label="⬇️ Download Data Quality Report (HTML)",
            data=f,
            file_name="online_retail_data_quality_report.html",
            mime="text/html",
        )

# --------------------------------------------------
# Project Artifacts
# --------------------------------------------------
st.subheader("📂 Project Artifacts")

if os.path.exists("cleaning_pipeline.py"):
    with open("cleaning_pipeline.py", "rb") as f:
        st.download_button(
            label="⬇️ Download AI Cleaning Pipeline (Python)",
            data=f,
            file_name="cleaning_pipeline.py",
            mime="text/x-python",
        )
