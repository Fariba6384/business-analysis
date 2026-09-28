# 📊 AI & Business Analytics Portfolio

> **Fariba Seyedjafarrangraz** · Business Transformation Analyst | Data & AI Enthusiast  
> CBAP Certified · PhD · 15+ Years in Banking & Higher Education Analytics

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-F7931E?style=flat&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=flat&logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 🧭 About This Repository

This portfolio showcases applied AI and analytics projects that bridge **business strategy** with **data science**. Each module addresses a real-world business challenge — from detecting financial fraud to forecasting supply chain demand — using Python, machine learning, and business intelligence techniques.

The work reflects 15+ years of experience across **banking**, **higher education**, and **enterprise IT**, with a focus on turning raw data into actionable decisions that drive operational efficiency and strategic value.

---

## 📁 Projects

### 🔍 Financial Risk & Fraud Detection
**File:** [`financial_risk_analysis.py`](financial_risk_analysis.py)

Detects anomalous banking transactions using **Isolation Forest** — an unsupervised ML algorithm built for fraud detection in high-volume, imbalanced datasets. Includes feature engineering (night-time flag, high-amount flag, combined risk score), StandardScaler normalization, anomaly scoring, and a tiered risk classification (High / Medium / Low).

- **Model:** `IsolationForest` (contamination=0.2, n_estimators=200)
- **Features:** Transaction amount, hour, location risk, derived signals
- **Output:** Per-transaction risk tier + AI insights and compliance flags

**Key concepts:** Anomaly detection · Unsupervised learning · Banking risk management

---

### 🚚 Smart Supply Chain — AI Risk & Demand Forecasting
**File:** [`supply_chain_forecasting.py`](supply_chain_forecasting.py)

An enterprise-grade supply chain intelligence platform that forecasts product demand across multiple scenarios and quantifies supplier risk using **Random Forest Regression**. Includes scenario analysis (Base / Growth / Risk), feature importance ranking, and strategic recommendations.

- **Model:** `RandomForestRegressor` (n=300, depth=12)
- **Features:** Marketing budget, inventory, shipping delays, supplier risk, seasonality, promo flag
- **Output:** Scenario forecasts, top demand drivers, operational KPIs

**Key concepts:** Demand forecasting · Scenario analysis · Supply chain optimization

---

### 📈 AI Business Analytics Dashboard
**File:** [`ai_business_dashboard.py`](ai_business_dashboard.py)

A customer analytics dashboard that computes sales KPIs, segments customers into performance tiers (Champion / Loyal / Potential / At Risk), runs regional analysis, and generates plain-language AI recommendations for retention and growth.

- **Segmentation:** Rule-based customer tiering from sales + satisfaction
- **Analysis:** Regional breakdown, repeat buyer rate, NPS-style insights
- **Output:** Structured BI dashboard with action items

**Key concepts:** Business intelligence · Customer segmentation · KPI reporting

---

### 🧠 Customer Insights Engine
**File:** [`customer_insights.py`](customer_insights.py)

Analyses customer satisfaction scores to compute benchmarks, estimate churn risk, generate an NPS proxy, and produce prioritised action items for the CRM team. Includes plan-level breakdown (Basic / Standard / Premium) and visual score bars.

- **Risk model:** Satisfaction + tenure → churn risk tier (High / Medium / Low)
- **Statistics:** Mean, median, std deviation, NPS proxy
- **Output:** Per-customer risk flags + ranked recommendations

**Key concepts:** Customer analytics · Churn prediction · CRM strategy

---

## 🛠️ Technologies Used

| Tool | Purpose |
|------|---------|
| **Python 3.10+** | Core language |
| **Pandas** | Data manipulation & analysis |
| **NumPy** | Numerical computing & simulation |
| **Scikit-learn** | Machine learning models |
| **Isolation Forest** | Anomaly / fraud detection |
| **Random Forest** | Demand forecasting & feature importance |
| **StandardScaler** | Feature normalization |
| **LabelEncoder** | Categorical encoding |

---

## 🚀 Getting Started

```bash
# Clone the repository
git clone https://github.com/Fariba6384/business-analysis.git
cd business-analysis

# Install dependencies
pip install -r requirements.txt

# Run any module
python financial_risk_analysis.py
python supply_chain_forecasting.py
python ai_business_dashboard.py
python customer_insights.py
```

---

## 🎯 Business Domains Covered

- 💳 **Financial Services** — Fraud detection, transaction risk scoring
- 🏭 **Supply Chain** — Demand forecasting, supplier risk management
- 👥 **Customer Analytics** — Satisfaction analysis, churn prediction, segmentation
- 📊 **Business Intelligence** — KPI dashboards, regional analysis, automated reporting

---

## 👤 About the Author

**Fariba Seyedjafarrangraz**  
Business Transformation Analyst · Dalhousie University, Registrar's Office  
Researcher · Sobey School of Business, Saint Mary's University

- 🎓 PhD | CBAP Certified
- 📍 Halifax, Nova Scotia, Canada
- 💼 15+ years in banking analytics & higher education data systems
- 🔧 Core tools: SQL · Power BI · Cognos · Banner · Python · Jira

> *"Turning data into decisions — one model at a time."*

---

## 📬 Contact

Feel free to connect or collaborate:  
📧 rangrazfariba6384@gmail.com  
🐙 [github.com/Fariba6384](https://github.com/Fariba6384)
