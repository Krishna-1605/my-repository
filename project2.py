# Monthly Budget
budget = float(input("Enter your monthly budget: "))

expenses = []   # list to store expenses
total_spent = 0

while True:
    name = input("Enter expense name (or type 'done' to finish): ")
    if name.lower() == "done":
        break

    amount = float(input("Enter expense amount: "))

    expenses.append((name, amount))
    total_spent += amount

print("\n----- EXPENSE SUMMARY -----")
for expense in expenses:
    print(f"{expense[0]} : ₹{expense[1]:.2f}")

remaining = budget - total_spent

print("---------------------------")
print(f"Total Spent     : ₹{total_spent:.2f}")
print(f"Remaining Budget: ₹{remaining:.2f}")
