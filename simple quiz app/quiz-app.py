# ==========================
# SIMPLE QUIZ APP
# ==========================

# Questions
questions = [
    "1. What is the capital of Ghana?",
    "2. Which language are you learning?",
    "3. How many days are in a week?",
    "4. Which planet do we live on?",
    "5. What does CPU stand for?"
]

# Options
options = [
    ["a. Kumasi", "b. Accra", "c. Takoradi"],
    ["a. Java", "b. Python", "c. C++"],
    ["a. 5", "b. 6", "c. 7"],
    ["a. Mars", "b. Earth", "c. Jupiter"],
    ["a. Central Processing Unit",
     "b. Computer Personal Unit",
     "c. Central Program Utility"]
]

# Correct answers
answers = ["b", "b", "c", "b", "a"]


# Function to run the quiz
def start_quiz():

    score = 0

    for i in range(len(questions)):

        print("\n" + questions[i])

        for option in options[i]:
            print(option)

        while True:

            answer = input("Enter your answer (a, b or c): ").lower()

            if answer in ["a", "b", "c"]:
                break

            else:
                print("Invalid option. Please enter a, b or c.")

        if answer == answers[i]:
            print("Correct!")
            score += 1

        else:
            print("Incorrect!")

    return score


# Main Program
while True:

    print("\n===== SIMPLE QUIZ APP =====")

    score = start_quiz()

    print("\n===== QUIZ COMPLETE =====")
    print(f"Your Score: {score}/{len(questions)}")

    play_again = input("\nPlay again? (y/n): ").lower()

    if play_again == "n":
        print("Thank you for playing!")
        break