# Monthly Budget
monthly_budget = float(input("Enter your monthly budget: "))

# Dictionary to store categorized expenses
categories = {
    "food": [],
    "travel": [],
    "utilities": [],
    "entertainment": [],
    "other": []
}

# List to store all expenses
expenses = []

# Function to add an expense
def add_expense(date, category, amount):
    expense = (date, category, amount)
    expenses.append(expense)

    if category in categories:
        categories[category].append(expense)
    else:
        categories["other"].append(expense)

# Adding sample expenses
add_expense("15-12-2025", "food", 4500.50,)
add_expense("16-12-2025", "travel", 2000.00)
add_expense("18-12-2025", "entertainment", 1500.00)
add_expense("17-12-2025", "utilities", 3500.00)

# Calculate total spent
total_spent = 0
for expense in expenses:
    total_spent += expense[2]

# Calculate category-wise totals
category_totals = {}
for category, items in categories.items():
    total = 0
    for expense in items:
        total += expense[2]
    category_totals[category] = total

# Calculate remaining budget
budget_remaining = monthly_budget - total_spent

# Calculate average daily expense
number_of_days = len(expenses)
average_daily_expense = total_spent / number_of_days

# Display Summary
print(f"""
========== EXPENSE TRACKER ==========
Monthly Budget: ₹{monthly_budget:,.0f}

Category-wise Spending:
---------------------------------
""")

for category, amount in category_totals.items():
    percent = (amount / monthly_budget) * 100
    print(f"{category.capitalize():15} ₹{amount:,.0f} ({percent:.0f}%)")

print(f"""---------------------------------
Total Spent:    ₹{total_spent:,.0f}
Remaining:     ₹{budget_remaining:,.0f}
Average Daily: ₹{average_daily_expense:,.0f}
=====================================
""")

# Budget Alerts
if total_spent > monthly_budget:
    print("🚨 ALERT: You are OVER your budget!")
elif total_spent > 0.8 * monthly_budget:
    print("⚠️ WARNING: You have used more than 80% of your budget.")
else:
    print("✅ You are within your budget.")
