# ==========================
# EXPENSE TRACKER
# ==========================

# List to store all expenses
expenses = []


# Function to add an expense
def add_expense(name, amount):
    expenses.append([name, amount])


# Function to display all expenses
def view_expenses():

    if len(expenses) == 0:
        print("No expenses recorded.")

    else:
        print("\nExpenses:")
        for expense in expenses:
            print(f"{expense[0]} - GHS {expense[1]:.2f}")


# Function to calculate total expenses
def total_expenses():

    total = 0

    for expense in expenses:
        total += expense[1]

    return total


# Main Program
while True:

    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Expenses")
    print("4. Exit")

    try:

        choice = int(input("Select an option: "))

        if choice == 1:

            name = input("Enter expense name: ")

            amount = float(input("Enter expense amount: GHS "))

            if amount > 0:
                add_expense(name, amount)
                print("Expense added successfully.")

            else:
                print("Amount must be greater than 0.")

        elif choice == 2:
            view_expenses()

        elif choice == 3:
            print(f"Total Expenses: GHS {total_expenses():.2f}")

        elif choice == 4:
            print("Thank you for using the Expense Tracker.")
            break

        else:
            print("Please select an option between 1 and 4.")

    except ValueError:
        print("Please enter a valid number.")