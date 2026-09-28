"""
financial_risk_analysis.py
===========================
AI-Powered Financial Fraud Detection System

Uses an Isolation Forest anomaly detection model to identify suspicious
banking transactions based on amount, timing, and location risk signals.

Author : Fariba Seyedjafarrangraz
         Business Transformation Analyst | CBAP | PhD
         Dalhousie University — Registrar's Office
         Halifax, Nova Scotia, Canada
"""

import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler


# ── 1. DATA ──────────────────────────────────────────────────────────────────

TRANSACTIONS = {
    "Transaction_ID":     [1001, 1002, 1003, 1004, 1005,
                           1006, 1007, 1008, 1009, 1010],
    "Transaction_Amount": [ 120,   85,  150, 2000,   95,
                            110, 5000,  130,  140, 7000],
    "Transaction_Hour":   [   9,   13,   15,    2,   11,
                              10,    1,   14,   16,    3],
    "Location_Risk":      [   1,    1,    1,    4,    1,
                               1,    5,    1,    1,    5],
}

df = pd.DataFrame(TRANSACTIONS)

# ── 2. FEATURE ENGINEERING ───────────────────────────────────────────────────

df["Is_Night"]      = (df["Transaction_Hour"] < 6).astype(int)
df["High_Amount"]   = (df["Transaction_Amount"] > 1000).astype(int)
df["Risk_Combined"] = df["Location_Risk"] * df["High_Amount"]

FEATURES = [
    "Transaction_Amount",
    "Transaction_Hour",
    "Location_Risk",
    "Is_Night",
    "Risk_Combined",
]

scaler  = StandardScaler()
X_scaled = scaler.fit_transform(df[FEATURES])

# ── 3. MODEL — ISOLATION FOREST ──────────────────────────────────────────────

model = IsolationForest(
    contamination=0.2,   # expect ~20 % anomalies
    n_estimators=200,
    random_state=42,
)
model.fit(X_scaled)

df["Anomaly_Score"]     = model.decision_function(X_scaled)   # lower = riskier
df["Fraud_Flag"]        = model.predict(X_scaled)             # -1 = suspicious
df["Fraud_Prediction"]  = df["Fraud_Flag"].map({1: "Normal", -1: "Suspicious"})

# Risk tier based on score
def risk_tier(score: float) -> str:
    if score < -0.10:
        return "HIGH RISK"
    elif score < 0.05:
        return "MEDIUM RISK"
    return "Low Risk"

df["Risk_Tier"] = df["Anomaly_Score"].apply(risk_tier)

# ── 4. ANALYSIS ──────────────────────────────────────────────────────────────

total       = len(df)
n_suspicious = (df["Fraud_Prediction"] == "Suspicious").sum()
fraud_pct   = n_suspicious / total * 100
suspicious  = df[df["Fraud_Prediction"] == "Suspicious"]

# ── 5. DASHBOARD OUTPUT ───────────────────────────────────────────────────────

DIVIDER = "─" * 60

def section(title: str) -> None:
    print(f"\n{'▌'} {title}")
    print(DIVIDER)

print("\n" + "═" * 60)
print("   AI FRAUD DETECTION DASHBOARD")
print("   Banking Transaction Risk Analysis")
print("═" * 60)

section("Full Transaction Log")
display_cols = [
    "Transaction_ID", "Transaction_Amount",
    "Transaction_Hour", "Location_Risk",
    "Fraud_Prediction", "Risk_Tier",
]
print(df[display_cols].to_string(index=False))

section("Summary KPIs")
print(f"  Total Transactions   : {total}")
print(f"  Normal               : {total - n_suspicious}")
print(f"  Suspicious Flagged   : {n_suspicious}")
print(f"  Fraud Risk Rate      : {fraud_pct:.1f}%")
print(f"  Avg Anomaly Score    : {df['Anomaly_Score'].mean():.4f}")

section("Suspicious Transactions — Detailed View")
print(
    suspicious[[
        "Transaction_ID", "Transaction_Amount",
        "Transaction_Hour", "Location_Risk", "Risk_Tier",
    ]].to_string(index=False)
)

section("AI Risk Insights & Recommendations")
insights = []

if fraud_pct > 15:
    insights.append("⚠  High anomaly rate detected — review model contamination threshold.")
if (df["Transaction_Amount"] > 3000).any():
    insights.append("⚠  Large-value transactions (>$3,000) require manual compliance review.")
if (df["Transaction_Hour"] < 5).any():
    insights.append("⚠  Off-hours transactions (00:00–05:00) show elevated fraud correlation.")
if (df["Location_Risk"] >= 4).any():
    insights.append("⚠  High location-risk codes detected — cross-reference with geofencing rules.")
if not insights:
    insights.append("✔  No critical risk signals detected in this batch.")

for insight in insights:
    print(f"  {insight}")

print("\n" + DIVIDER)
print("  Analysis complete.")
print(DIVIDER + "\n")
