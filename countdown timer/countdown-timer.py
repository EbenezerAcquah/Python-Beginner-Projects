#Import the time modulde
import time

try:
    seconds = int(input("Enter the countdown time in seconds: "))

#Keep on printing to the screen and pause the program for 1s as long as time is greater than 0
    while seconds > 0:
        print(seconds)
        time.sleep(1)
        seconds -= 1

    print("Time's Up")

#Runs if user enters something that cannot to converted to an integer 
except ValueError:
    print ("Please enter a valid number!")