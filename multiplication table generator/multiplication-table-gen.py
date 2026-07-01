# ==========================
# MULTIPLICATION TABLE GENERATOR
# ==========================

# Function to generate the multiplication table
def multiplication_table(number):

    # Loop from 1 to 12
    for i in range(1, 13):

        # Display each multiplication
        print(f"{number} x {i} = {number * i}")


print("===== MULTIPLICATION TABLE GENERATOR =====")

try:

    # Ask the user for a number
    number = int(input("Enter a number: "))

    # Call the function
    multiplication_table(number)

except ValueError:

    # Handle invalid input
    print("Please enter a valid whole number.")