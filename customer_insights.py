"""
customer_insights.py
====================
Customer Satisfaction Intelligence Engine

Analyses customer satisfaction scores, computes benchmarks,
identifies outliers, scores churn risk, and outputs prioritised
action items — designed to inform CRM and retention strategy.

Author : Fariba Seyedjafarrangraz
         Business Transformation Analyst | CBAP | PhD
         Dalhousie University — Registrar's Office
         Halifax, Nova Scotia, Canada
"""

import statistics


# ── 1. DATA ──────────────────────────────────────────────────────────────────

CUSTOMERS = [
    {"id": "C001", "name": "Ali",   "satisfaction": 4.5, "tenure_months": 18, "plan": "Premium"},
    {"id": "C002", "name": "Sara",  "satisfaction": 3.8, "tenure_months":  6, "plan": "Basic"},
    {"id": "C003", "name": "Reza",  "satisfaction": 4.9, "tenure_months": 36, "plan": "Premium"},
    {"id": "C004", "name": "Mina",  "satisfaction": 4.2, "tenure_months": 12, "plan": "Standard"},
    {"id": "C005", "name": "David", "satisfaction": 2.9, "tenure_months":  3, "plan": "Basic"},
    {"id": "C006", "name": "Lena",  "satisfaction": 4.7, "tenure_months": 24, "plan": "Premium"},
    {"id": "C007", "name": "Omar",  "satisfaction": 3.5, "tenure_months":  8, "plan": "Standard"},
    {"id": "C008", "name": "Nina",  "satisfaction": 4.1, "tenure_months": 15, "plan": "Standard"},
]

# ── 2. SCORING & SEGMENTATION ─────────────────────────────────────────────────

def satisfaction_label(score: float) -> str:
    if score >= 4.5:   return "Excellent"
    elif score >= 4.0: return "Good"
    elif score >= 3.5: return "Fair"
    return "Poor"

def churn_risk(score: float, tenure: int) -> str:
    """Estimate churn risk from satisfaction and tenure."""
    if score < 3.5 and tenure < 6:   return "🔴 HIGH"
    elif score < 4.0 or tenure < 6:  return "🟡 MEDIUM"
    return "🟢 LOW"

for c in CUSTOMERS:
    c["label"]      = satisfaction_label(c["satisfaction"])
    c["churn_risk"] = churn_risk(c["satisfaction"], c["tenure_months"])

# ── 3. STATISTICS ─────────────────────────────────────────────────────────────

scores     = [c["satisfaction"] for c in CUSTOMERS]
avg_score  = statistics.mean(scores)
med_score  = statistics.median(scores)
std_score  = statistics.stdev(scores)
min_score  = min(scores)
max_score  = max(scores)

high_risk_customers  = [c for c in CUSTOMERS if "HIGH"   in c["churn_risk"]]
med_risk_customers   = [c for c in CUSTOMERS if "MEDIUM" in c["churn_risk"]]

# NPS proxy: promoters ≥4.5, detractors <3.5
promoters  = [c for c in CUSTOMERS if c["satisfaction"] >= 4.5]
detractors = [c for c in CUSTOMERS if c["satisfaction"] <  3.5]
nps_proxy  = (len(promoters) - len(detractors)) / len(CUSTOMERS) * 100

# ── 4. PLAN-LEVEL ANALYSIS ────────────────────────────────────────────────────

from collections import defaultdict

plan_scores: dict = defaultdict(list)
for c in CUSTOMERS:
    plan_scores[c["plan"]].append(c["satisfaction"])

plan_summary = {
    plan: {
        "avg": round(statistics.mean(vals), 2),
        "count": len(vals),
    }
    for plan, vals in sorted(plan_scores.items())
}

# ── 5. ACTION ITEMS ───────────────────────────────────────────────────────────

def action_items(customers: list) -> list[str]:
    actions = []
    highs = [c["name"] for c in customers if "HIGH" in c["churn_risk"]]
    meds  = [c["name"] for c in customers if "MEDIUM" in c["churn_risk"]]
    if highs:
        actions.append(f"🔴 Immediate outreach required: {', '.join(highs)}")
    if meds:
        actions.append(f"🟡 Schedule check-in calls: {', '.join(meds)}")
    if nps_proxy < 0:
        actions.append("⚠  NPS proxy is negative — launch satisfaction recovery programme.")
    if avg_score < 4.0:
        actions.append("◉ Overall satisfaction below target — review service delivery quality.")
    best = max(customers, key=lambda c: c["satisfaction"])
    actions.append(f"✔ Highlight {best['name']} as a potential case study / testimonial.")
    return actions

# ── 6. DASHBOARD OUTPUT ───────────────────────────────────────────────────────

DIVIDER = "─" * 65

def section(title: str) -> None:
    print(f"\n{'▌'} {title}")
    print(DIVIDER)

print("\n" + "═" * 65)
print("   CUSTOMER SATISFACTION INTELLIGENCE ENGINE")
print("   Retention Risk & Experience Analytics")
print("═" * 65)

section("Customer Satisfaction Scores")
header = f"  {'ID':<6} {'Name':<8} {'Score':>6}  {'Level':<10}  {'Plan':<10}  {'Tenure':>7}  Risk"
print(header)
print("  " + "-" * 62)
for c in CUSTOMERS:
    print(
        f"  {c['id']:<6} {c['name']:<8} {c['satisfaction']:>6.1f}"
        f"  {c['label']:<10}  {c['plan']:<10}  {c['tenure_months']:>5} mo  {c['churn_risk']}"
    )

section("Statistical Summary")
print(f"  Average Score     : {avg_score:.2f} / 5.00")
print(f"  Median Score      : {med_score:.2f}")
print(f"  Std Deviation     : {std_score:.2f}")
print(f"  Range             : {min_score} – {max_score}")
print(f"  NPS Proxy         : {nps_proxy:+.0f}")

section("Subscription Plan Breakdown")
for plan, info in plan_summary.items():
    bar = "█" * int(info["avg"] * 2)
    print(f"  {plan:<10} | Avg: {info['avg']:.2f}  n={info['count']}  {bar}")

section("Churn Risk Summary")
print(f"  🔴 High Risk     : {len(high_risk_customers)} customer(s)")
print(f"  🟡 Medium Risk   : {len(med_risk_customers)} customer(s)")
print(f"  🟢 Low Risk      : {len(CUSTOMERS) - len(high_risk_customers) - len(med_risk_customers)} customer(s)")

section("Recommended Actions")
for action in action_items(CUSTOMERS):
    print(f"  {action}")

print("\n" + DIVIDER)
print("  Analysis complete.")
print(DIVIDER + "\n")
