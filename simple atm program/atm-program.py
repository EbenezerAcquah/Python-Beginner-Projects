# Starting account balance
account_balance = 100

# Function to deposit money
def deposit_amount(account_balance, amount):
    return account_balance + amount

# Function to withdraw money
def withdrawal(account_balance, amount):
    return account_balance - amount


while True:
    print("\n== SIMPLE ATM MACHINE ==")
    print("1. Check Balance")
    print("2. Deposit Amount")
    print("3. Withdraw Amount")
    print("4. Exit")

    try:
        # Ask the user to choose an option
        choice = int(input("Select an option: "))

        # Option 1: Check Balance
        if choice == 1:
            print(f"Current Balance: GHS {account_balance}")

        # Option 2: Deposit Money
        elif choice == 2:
            amount = float(input("Enter amount to deposit: "))

            if amount > 0:
                account_balance = deposit_amount(account_balance, amount)
                print(f"Your deposit of GHS {amount} was successful.")
                print(f"New Balance: GHS {account_balance}")
            else:
                print("Deposit amount must be greater than 0.")

        # Option 3: Withdraw Money
        elif choice == 3:
            amount = float(input("Enter amount to withdraw: "))

            if amount <= 0:
                print("Withdrawal amount must be greater than 0.")

            elif amount <= account_balance:
                account_balance = withdrawal(account_balance, amount)
                print("Withdrawal was successful.")
                print(f"New Balance: GHS {account_balance}")

            else:
                print("You have insufficient funds to perform this transaction.")

        # Option 4: Exit
        elif choice == 4:
            print("Thank you for using the ATM.")
            break

        # Invalid menu option
        else:
            print("Please select an option between 1 and 4.")

    except ValueError:
        print("Invalid input. Please enter numbers only.")