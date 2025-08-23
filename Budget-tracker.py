# budget_tracker.py
# Simple Budget Tracker by Katie

import os

income_list = []
expense_list = []

def add_income():
    try:
        amount = float(input("Enter income amount: $"))
        income_list.append(amount)
        print(f"✅ Added ${amount:.2f} to income.\n")
    except ValueError:
        print("❌ Please enter a valid number.\n")

def add_expense():
    try:
        amount = float(input("Enter expense amount: $"))
        expense_list.append(amount)
        print(f"✅ Added ${amount:.2f} to expenses.\n")
    except ValueError:
        print("❌ Please enter a valid number.\n")

def show_summary():
    total_income = sum(income_list)
    total_expense = sum(expense_list)
    balance = total_income - total_expense

    print("\n📊 --- Budget Summary ---")
    print(f"Total Income:   ${total_income:.2f}")
    print(f"Total Expenses: ${total_expense:.2f}")
    print(f"Balance:        ${balance:.2f}")
    print("---------------------------\n")

def save_to_file():
    total_income = sum(income_list)
    total_expense = sum(expense_list)
    balance = total_income - total_expense

    with open("budget_summary.txt", "w") as file:
        file.write("📊 Budget Summary\n")
        file.write("---------------------------\n")
        file.write(f"Total Income:   ${total_income:.2f}\n")
        file.write(f"Total Expenses: ${total_expense:.2f}\n")
        file.write(f"Balance:        ${balance:.2f}\n")
        file.write("---------------------------\n")

    print("💾 Budget summary saved to budget_summary.txt\n")

while True:
    print("Select an option:")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. Show Summary")
    print("4. Save to File")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        add_income()
    elif choice == '2':
        add_expense()
    elif choice == '3':
        show_summary()
    elif choice == '4':
        save_to_file()
    elif choice == '5':
        print("👋 Goodbye! Keep tracking your budget!")
        break
    
