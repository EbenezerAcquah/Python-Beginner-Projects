# ==========================
# ROCK, PAPER, SCISSORS
# ==========================

import random


# Function to determine the winner
def determine_winner(player, computer):

    if player == computer:
        return "It's a draw!"

    elif player == "rock" and computer == "scissors":
        return "You win!"

    elif player == "paper" and computer == "rock":
        return "You win!"

    elif player == "scissors" and computer == "paper":
        return "You win!"

    else:
        return "Computer wins!"


choices = ["rock", "paper", "scissors"]

while True:

    print("\n===== ROCK, PAPER, SCISSORS =====")

    player = input("Choose Rock, Paper or Scissors: ").lower()

    if player not in choices:
        print("Invalid choice.")
        continue

    computer = random.choice(choices)

    print(f"\nYou chose: {player.capitalize()}")
    print(f"Computer chose: {computer.capitalize()}")

    result = determine_winner(player, computer)

    print(result)

    play_again = input("\nPlay again? (y/n): ").lower()

    if play_again == "n":
        print("Thank you for playing!")
        break