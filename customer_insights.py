
customers = [
    {"name": "Ali", "satisfaction": 4.5},
    {"name": "Sara", "satisfaction": 3.8},
    {"name": "Reza", "satisfaction": 4.9},
    {"name": "Mina", "satisfaction": 4.2}
]

total = 0

for customer in customers:
    total += customer["satisfaction"]

average_score = total / len(customers)

print("Customer Satisfaction Analysis")
print("-" * 35)

for customer in customers:
    print(f"{customer['name']} : {customer['satisfaction']}")

print("-" * 35)
print(f"Average Satisfaction Score: {average_score:.2f}")

if average_score >= 4:
    print("Customer satisfaction level is strong.")
else:
    print("Customer satisfaction needs improvement.")
