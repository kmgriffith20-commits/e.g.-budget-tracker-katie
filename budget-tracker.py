# budget_tracker.py
# Simple Budget Tracker by Katie

print("Welcome to Katie's Budget Tracker!\n")

# Initialize empty lists for income and expenses
income_list = []
expense_list = []

def add_income():
    try:
        amount = float(input("Enter income amount: $"))
        income_list.append(amount)
        print(f"Added ${amount:.2f} to income.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def add_expense():
    try:
        amount = float(input("Enter expense amount: $"))
        expense_list.append(amount)
        print(f"Added ${amount:.2f} to expenses.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def show_summary():
    total_income = sum(income_list)
    total_expense = sum(expense_list)
    balance = total_income - total_expense

    print("\n--- Budget Summary ---")
    print(f"Total Income: ${total_income:.2f}")
    print(f"Total Expenses: ${total_expense:.2f}")
    print(f"Balance: ${balance:.2f}\n")

while True:
    print("Select an option:")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. Show Summary")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        add_income()
    elif choice == '2':
        add_expense()
    elif choice == '3':
        show_summary()
    elif choice == '4':
        print("Goodbye! Keep tracking your budget!")
        break
    else:
        print("Invalid choice, please select 1-4.\n")
