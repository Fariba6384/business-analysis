"""
supply_chain_forecasting.py
============================
AI Supply Chain Risk & Demand Forecasting Platform

Simulates an enterprise supply chain dataset and applies a
Random Forest Regressor to forecast product demand, quantify
supplier risk, and surface strategic operational insights.

Author : Fariba Seyedjafarrangraz
         Business Transformation Analyst | CBAP | PhD
         Dalhousie University — Registrar's Office
         Halifax, Nova Scotia, Canada
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.preprocessing import LabelEncoder


# ── 1. SYNTHETIC DATASET ─────────────────────────────────────────────────────

np.random.seed(42)

PRODUCTS = [
    "Laptop", "Phone", "Tablet", "Monitor",
    "Keyboard", "Mouse", "Printer", "Camera",
    "Speaker", "Smartwatch",
]

dates = pd.date_range(start="2024-01-01", periods=120, freq="D")

records = []
for date in dates:
    for product in PRODUCTS:
        marketing      = np.random.randint(1_000, 5_000)
        inventory      = np.random.randint(50, 500)
        shipping_delay = np.random.randint(0, 10)
        supplier_risk  = np.random.randint(1, 6)
        seasonality    = np.random.randint(1, 5)
        promo_flag     = int(np.random.rand() > 0.8)    # 20 % chance of promotion

        demand = (
            marketing      * 0.80
            + inventory    * 1.50
            - shipping_delay * 120
            - supplier_risk  * 200
            + seasonality    * 300
            + promo_flag     * 800
            + np.random.normal(0, 500)
        )

        records.append({
            "Date":                date,
            "Product":             product,
            "Marketing_Budget":    marketing,
            "Inventory_Level":     inventory,
            "Shipping_Delay_Days": shipping_delay,
            "Supplier_Risk_Score": supplier_risk,
            "Seasonality_Index":   seasonality,
            "Promo_Flag":          promo_flag,
            "Demand":              max(0, round(demand)),
        })

df = pd.DataFrame(records)

# ── 2. FEATURE ENGINEERING ───────────────────────────────────────────────────

df["Month"]           = df["Date"].dt.month
df["Quarter"]         = df["Date"].dt.quarter
df["DayOfWeek"]       = df["Date"].dt.dayofweek
df["Demand_per_Marketing"] = df["Demand"] / (df["Marketing_Budget"] + 1)

le = LabelEncoder()
df["Product_Enc"] = le.fit_transform(df["Product"])

FEATURES = [
    "Marketing_Budget", "Inventory_Level", "Shipping_Delay_Days",
    "Supplier_Risk_Score", "Seasonality_Index", "Promo_Flag",
    "Month", "Quarter", "DayOfWeek", "Product_Enc",
]

X = df[FEATURES]
y = df["Demand"]

# ── 3. TRAIN / TEST SPLIT & MODEL ────────────────────────────────────────────

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor(
    n_estimators=300,
    max_depth=12,
    min_samples_split=5,
    random_state=42,
    n_jobs=-1,
)
model.fit(X_train, y_train)

preds = model.predict(X_test)
mae   = mean_absolute_error(y_test, preds)
r2    = r2_score(y_test, preds)

# ── 4. FUTURE DEMAND FORECAST ────────────────────────────────────────────────

SCENARIOS = {
    "Base Case":      {"Marketing_Budget": 3000, "Promo_Flag": 0, "Supplier_Risk_Score": 3},
    "Growth Push":    {"Marketing_Budget": 4800, "Promo_Flag": 1, "Supplier_Risk_Score": 2},
    "Risk Scenario":  {"Marketing_Budget": 2000, "Promo_Flag": 0, "Supplier_Risk_Score": 5},
}

COMMON = {
    "Inventory_Level": 320, "Shipping_Delay_Days": 2,
    "Seasonality_Index": 4, "Month": 9,
    "Quarter": 3, "DayOfWeek": 2, "Product_Enc": 0,
}

scenario_forecasts = {}
for name, overrides in SCENARIOS.items():
    row = {**COMMON, **overrides}
    scenario_forecasts[name] = model.predict(pd.DataFrame([row]))[0]

# ── 5. OPERATIONAL RISK ANALYSIS ─────────────────────────────────────────────

high_risk   = df[df["Supplier_Risk_Score"] >= 4]
avg_delay   = df["Shipping_Delay_Days"].mean()
top_product = (
    df.groupby("Product")["Demand"]
    .mean()
    .sort_values(ascending=False)
)

# ── 6. FEATURE IMPORTANCE ────────────────────────────────────────────────────

importance_df = (
    pd.DataFrame({
        "Feature":    FEATURES,
        "Importance": model.feature_importances_,
    })
    .sort_values("Importance", ascending=False)
    .reset_index(drop=True)
)

# ── 7. DASHBOARD OUTPUT ───────────────────────────────────────────────────────

DIVIDER = "─" * 70

def section(title: str) -> None:
    print(f"\n{'▌'} {title}")
    print(DIVIDER)

print("\n" + "═" * 70)
print("   AI SUPPLY CHAIN INTELLIGENCE PLATFORM")
print("   Demand Forecasting & Supplier Risk Analytics")
print("═" * 70)

section("Dataset Overview")
print(f"  Records   : {len(df):,}")
print(f"  Products  : {df['Product'].nunique()}")
print(f"  Date Range: {df['Date'].min().date()} → {df['Date'].max().date()}")
print(f"  Avg Demand: {df['Demand'].mean():,.0f} units / record")

section("Model Performance")
print(f"  Algorithm         : Random Forest Regressor (n=300, depth=12)")
print(f"  Train / Test Split: 80 % / 20 %")
print(f"  Mean Absolute Error: {mae:,.0f} units")
print(f"  R² Score           : {r2:.4f}")

section("Demand Forecast — Scenario Analysis")
for scenario, forecast in scenario_forecasts.items():
    bar = "█" * int(forecast / 500)
    print(f"  {scenario:<18}: {forecast:>8,.0f} units  {bar}")

section("Operational KPIs")
print(f"  Avg Shipping Delay       : {avg_delay:.2f} days")
print(f"  High-Risk Supplier Rows  : {len(high_risk):,} / {len(df):,}")
print(f"  High-Risk %              : {len(high_risk)/len(df)*100:.1f}%")

section("Top Products by Average Demand")
for rank, (product, demand) in enumerate(top_product.head(5).items(), 1):
    print(f"  {rank}. {product:<12} : {demand:,.0f} units")

section("Top Predictive Business Drivers")
for _, row in importance_df.head(8).iterrows():
    bar = "█" * int(row["Importance"] * 60)
    print(f"  {row['Feature']:<25} {row['Importance']:.4f}  {bar}")

section("Strategic AI Insights")
recommendations = []
if avg_delay > 5:
    recommendations.append("⚠  Average shipping delay exceeds 5 days — review logistics contracts.")
if len(high_risk) / len(df) > 0.20:
    recommendations.append("⚠  >20 % supplier risk exposure — prioritise diversification.")
if scenario_forecasts["Growth Push"] > scenario_forecasts["Base Case"] * 1.3:
    recommendations.append("✔  Promotional campaigns deliver >30 % demand uplift — scale budget.")
if r2 > 0.85:
    recommendations.append("✔  Model explains >85 % of demand variance — suitable for production use.")
recommendations.append(f"◉  Focus inventory builds on '{top_product.index[0]}' — highest avg demand.")

for rec in recommendations:
    print(f"  {rec}")

print("\n" + DIVIDER)
print("  Analysis complete.")
print(DIVIDER + "\n")
