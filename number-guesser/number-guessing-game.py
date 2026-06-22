#importing the random module
import random 

#Picks and store any random number between 1 and 100
secretNumber = random.randint(1, 100)
attempts = 0

print("== NUMBER GUESSING GAME ==")
print ("Guess a number between 1 and 100")

while True:
    #code to try
    try:
        guess = int(input("Enter your guess: "))

        #Prevents users from entering numbers outside 1–100.
        if not 1 <= guess <= 100:
            print("Enter a valid number")
            continue

        attempts += 1

        if guess < secretNumber:
            print ("Too Low!")

        elif guess > secretNumber:
            print ("Too High!")

        else:
            print ("Congratulations, you got it right!!!!")
            if attempts == 1:
                print ("Wow, it took you " + str(attempts) +" attempt to guess it right")
            else:
                print ("It took you " + str(attempts) +" attempts to guess it right")
            break

    #code to run when an error occurs
    except ValueError:
        print ("Please enter a valid number")

        