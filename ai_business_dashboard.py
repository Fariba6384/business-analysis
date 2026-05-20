import pandas as pd

# Sample business data
data = {
    "Customer": ["Ali", "Sara", "Reza", "Mina", "David"],
    "Sales": [1200, 950, 1750, 1100, 2100],
    "Satisfaction": [4.5, 3.9, 4.8, 4.1, 4.9]
}

# Create DataFrame
df = pd.DataFrame(data)

# Business analytics
total_sales = df["Sales"].sum()
average_sales = df["Sales"].mean()
average_satisfaction = df["Satisfaction"].mean()

# Simple AI-style insight generation
if average_satisfaction >= 4.5:
    insight = "Customer satisfaction is excellent."
elif average_satisfaction >= 4:
    insight = "Customer satisfaction is good."
else:
    insight = "Customer satisfaction needs improvement."

# Dashboard output
print("AI Business Analytics Dashboard")
print("=" * 40)

print("\nCustomer Data:")
print(df)

print("\nBusiness Insights")
print("-" * 40)
print(f"Total Sales: ${total_sales}")
print(f"Average Sales: ${average_sales:.2f}")
print(f"Average Satisfaction: {average_satisfaction:.2f}")

print("\nAI Recommendation")
print("-" * 40)
print(insight)

# Top customer analysis
top_customer = df.loc[df["Sales"].idxmax()]

print("\nTop Customer")
print("-" * 40)
print(f"Name: {top_customer['Customer']}")
print(f"Sales: ${top_customer['Sales']}")
