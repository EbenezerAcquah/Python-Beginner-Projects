# Password Generator

# Import the random module
import random

# Function to generate the password
def generate_password(length):

    # Store all the characters that can be used
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"

    # Start with an empty password
    password = ""

    # Repeat according to the length entered by the user
    for i in range(length):

        # Pick a random character
        random_character = random.choice(characters)

        # Add the character to the password
        password += random_character

    # Return the completed password
    return password



print("==== PASSWORD GENERATOR ====") 

try:

    # Ask the user for the password length
    length = int(input("Enter the password length: "))

    # Check that the length is valid
    if length <= 0:
        print("Password length must be greater than 0.")

    else:

        # Generate the password
        password = generate_password(length)

        # Display the password
        print(f"\nYour password is:\n{password}")

except ValueError:
    print("Please enter a valid number.")
