"""
ai_business_dashboard.py
=========================
AI-Powered Business Analytics Dashboard

Aggregates customer sales and satisfaction data, computes KPIs,
segments customers by performance tier, and generates plain-language
business insights — ready to extend into a live BI dashboard.

Author : Fariba Seyedjafarrangraz
         Business Transformation Analyst | CBAP | PhD
         Dalhousie University — Registrar's Office
         Halifax, Nova Scotia, Canada
"""

import pandas as pd


# ── 1. DATA ──────────────────────────────────────────────────────────────────

CUSTOMERS = {
    "Customer":     ["Ali",  "Sara", "Reza", "Mina", "David",
                     "Lena", "Omar", "Nina", "Jake", "Yuki"],
    "Region":       ["East", "West", "East", "North", "West",
                     "South","East", "West", "North", "South"],
    "Sales":        [1200,    950,   1750,   1100,   2100,
                      870,   1430,   1960,    780,   2250],
    "Satisfaction": [ 4.5,    3.9,    4.8,    4.1,    4.9,
                      3.7,    4.3,    4.7,    3.5,    5.0],
    "Repeat_Buyer": [True,  False,   True,   True,  False,
                     False,  True,   True,  False,   True],
}

df = pd.DataFrame(CUSTOMERS)

# ── 2. KPI COMPUTATION ───────────────────────────────────────────────────────

total_sales        = df["Sales"].sum()
avg_sales          = df["Sales"].mean()
median_sales       = df["Sales"].median()
avg_satisfaction   = df["Satisfaction"].mean()
repeat_rate        = df["Repeat_Buyer"].mean() * 100
top_customer       = df.loc[df["Sales"].idxmax()]
lowest_satisfaction = df.loc[df["Satisfaction"].idxmin()]

# ── 3. CUSTOMER SEGMENTATION ─────────────────────────────────────────────────

def segment(row: pd.Series) -> str:
    if row["Sales"] >= 1800 and row["Satisfaction"] >= 4.5:
        return "⭐ Champion"
    elif row["Sales"] >= 1200 and row["Satisfaction"] >= 4.0:
        return "✔ Loyal"
    elif row["Sales"] < 1000 or row["Satisfaction"] < 4.0:
        return "⚡ At Risk"
    return "◉ Potential"

df["Segment"] = df.apply(segment, axis=1)

# ── 4. REGIONAL SUMMARY ──────────────────────────────────────────────────────

regional = (
    df.groupby("Region")
    .agg(
        Total_Sales   = ("Sales", "sum"),
        Avg_Sat       = ("Satisfaction", "mean"),
        Customers     = ("Customer", "count"),
    )
    .sort_values("Total_Sales", ascending=False)
)

# ── 5. AI INSIGHT ENGINE ─────────────────────────────────────────────────────

def generate_insights(df: pd.DataFrame, avg_sat: float, repeat_rate: float) -> list[str]:
    insights = []
    if avg_sat >= 4.5:
        insights.append("✔ Customer satisfaction is EXCELLENT — leverage for referral programmes.")
    elif avg_sat >= 4.0:
        insights.append("◉ Satisfaction is GOOD — focus on converting 'At Risk' customers.")
    else:
        insights.append("⚠ Satisfaction NEEDS IMPROVEMENT — initiate customer recovery plan.")

    at_risk = df[df["Segment"] == "⚡ At Risk"]
    if len(at_risk):
        names = ", ".join(at_risk["Customer"].tolist())
        insights.append(f"⚠ {len(at_risk)} at-risk customer(s): {names} — prioritise outreach.")

    if repeat_rate >= 60:
        insights.append(f"✔ Repeat purchase rate {repeat_rate:.0f}% is strong — expand loyalty rewards.")
    else:
        insights.append(f"⚡ Repeat rate {repeat_rate:.0f}% is low — consider retention campaign.")

    low_reg = regional["Total_Sales"].idxmin()
    insights.append(f"◉ Region '{low_reg}' has the lowest sales — investigate market barriers.")

    return insights

insights = generate_insights(df, avg_satisfaction, repeat_rate)

# ── 6. DASHBOARD OUTPUT ───────────────────────────────────────────────────────

DIVIDER = "─" * 65

def section(title: str) -> None:
    print(f"\n{'▌'} {title}")
    print(DIVIDER)

print("\n" + "═" * 65)
print("   AI BUSINESS ANALYTICS DASHBOARD")
print("   Customer Sales & Satisfaction Intelligence")
print("═" * 65)

section("Customer Overview")
print(
    df[[
        "Customer", "Region", "Sales",
        "Satisfaction", "Repeat_Buyer", "Segment",
    ]].to_string(index=False)
)

section("Key Performance Indicators")
print(f"  Total Revenue          : ${total_sales:,.0f}")
print(f"  Average Sales / Client : ${avg_sales:,.2f}")
print(f"  Median Sales           : ${median_sales:,.0f}")
print(f"  Avg Satisfaction Score : {avg_satisfaction:.2f} / 5.00")
print(f"  Repeat Buyer Rate      : {repeat_rate:.1f}%")

section("Top Performer")
print(f"  Customer   : {top_customer['Customer']}")
print(f"  Sales      : ${top_customer['Sales']:,}")
print(f"  Sat. Score : {top_customer['Satisfaction']}")
print(f"  Segment    : {top_customer['Segment']}")

section("Regional Performance")
print(regional.to_string())

section("Customer Segments")
seg_counts = df["Segment"].value_counts()
for seg, count in seg_counts.items():
    print(f"  {seg:<18} : {count} customer(s)")

section("AI Recommendations")
for insight in insights:
    print(f"  {insight}")

print("\n" + DIVIDER)
print("  Dashboard complete.")
print(DIVIDER + "\n")
