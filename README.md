# 🧹 AI Data Quality & Cleaning Assistant

An AI-powered data quality and cleaning assistant built with **Streamlit** and **LLMs**.  
The app analyzes uploaded CSV datasets, highlights data quality issues, explains business impact, and generates production-ready Pandas cleaning pipelines.

---

## 🚀 Features

- 📤 Upload any CSV dataset
- 🧠 AI-generated data quality insights
- 📊 Business impact analysis of data issues
- 🧪 Automated Pandas data-cleaning code
- 📥 Downloadable offline data profiling report (HTML)
- ☁️ Deployed on Streamlit Cloud

---

## 🏗️ Tech Stack

- **Python**
- **Streamlit**
- **Pandas**
- **OpenAI API (LLMs)**

---

## 📂 Project Structure

ai-data-quality-assistant/
├── app.py
├── requirements.txt
├── cleaning_pipeline.py
├── online_retail_data_quality_report.html
└── .streamlit/
├── config.toml
└── secrets.toml


---

## 🔑 Environment Variables

Create `.streamlit/secrets.toml`:

```toml
OPENAI_API_KEY = "your_openai_api_key"

