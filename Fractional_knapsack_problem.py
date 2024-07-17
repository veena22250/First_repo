# Define the items with their respective profits and weights
items = [
    {"profit": 20, "weight": 5},
    {"profit": 30, "weight": 8},
    {"profit": 40, "weight": 10},
    {"profit": 32, "weight": 12},
    {"profit": 55, "weight": 15},
]

# Calculate the value-to-weight ratio and sort items by this ratio in descending order
for item in items:
    item["ratio"] = item["profit"] / item["weight"]

items = sorted(items, key=lambda x: x["ratio"], reverse=True)

# Maximum Knapsack capacity
capacity = 20
total_value = 0
total_weight = 0

# Implementing the Fractional Knapsack algorithm
for item in items:
    if total_weight + item["weight"] <= capacity:
        # Add the whole item to the knapsack
        total_weight += item["weight"]
        total_value += item["profit"]
    else:
        # Add fractional part of the item to the knapsack
        remaining_capacity = capacity - total_weight
        total_value += item["ratio"] * remaining_capacity
        total_weight += remaining_capacity
        break



(total_value, total_weight)

print(total_value,total_weight)
