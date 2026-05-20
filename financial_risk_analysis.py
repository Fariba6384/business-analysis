import pandas as pd
from sklearn.ensemble import IsolationForest

# -----------------------------------
# Financial Fraud Detection System
# -----------------------------------

# Sample banking transaction data
data = {
    "Transaction_ID": range(1001, 1011),
    "Transaction_Amount": [120, 85, 150, 2000, 95, 110, 5000, 130, 140, 7000],
    "Transaction_Hour": [9, 13, 15, 2, 11, 10, 1, 14, 16, 3],
    "Location_Risk": [1, 1, 1, 4, 1, 1, 5, 1, 1, 5]
}

# Create DataFrame
df = pd.DataFrame(data)

# Features for AI model
features = df[[
    "Transaction_Amount",
    "Transaction_Hour",
    "Location_Risk"
]]

# Train anomaly detection model
model = IsolationForest(
    contamination=0.2,
    random_state=42
)

df["Fraud_Prediction"] = model.fit_predict(features)

# Convert predictions
df["Fraud_Prediction"] = df["Fraud_Prediction"].map({
    1: "Normal",
    -1: "Suspicious"
})

# -----------------------------------
# Risk Analysis
# -----------------------------------

suspicious_transactions = df[
    df["Fraud_Prediction"] == "Suspicious"
]

total_transactions = len(df)
fraud_count = len(suspicious_transactions)

fraud_percentage = (
    fraud_count / total_transactions
) * 100

# -----------------------------------
# AI Dashboard Output
# -----------------------------------

print("\nAI FRAUD DETECTION DASHBOARD")
print("=" * 55)

print("\nTransaction Dataset")
print("-" * 55)
print(df)

print("\nFraud Analysis Summary")
print("-" * 55)

print(f"Total Transactions: {total_transactions}")
print(f"Suspicious Transactions: {fraud_count}")
print(f"Fraud Risk Percentage: {fraud_percentage:.2f}%")

print("\nSuspicious Transactions")
print("-" * 55)

print(
    suspicious_transactions[
        [
            "Transaction_ID",
            "Transaction_Amount",
            "Transaction_Hour"
        ]
    ]
)

print("\nAI Risk Insights")
print("-" * 55)

if fraud_percentage > 15:
    print("Warning: High anomaly activity detected.")

high_risk_amounts = df[
    df["Transaction_Amount"] > 3000
]

if len(high_risk_amounts) > 0:
    print("Large financial transactions require manual review.")

night_transactions = df[
    df["Transaction_Hour"] < 5
]

if len(night_transactions) > 0:
    print("Late-night transactions show elevated fraud risk.")
