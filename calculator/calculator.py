#Defining functions for the operations

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Division by zero is not allowed"
    return a / b

#Give options to choose from

print("Simple Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Choose operation: "))

#Take user's values

FirstNumber = float(input("Enter first number: "))
SecondNumber = float(input("Enter second number: "))

if choice == 1:
    print(add(FirstNumber , SecondNumber))

elif choice == 2:
    print(subtract(FirstNumber , SecondNumber))

elif choice == 3:
    print(multiply(FirstNumber, SecondNumber))

elif choice == 4:
    print(divide(FirstNumber, SecondNumber))

else:
    print("Invalid choice")