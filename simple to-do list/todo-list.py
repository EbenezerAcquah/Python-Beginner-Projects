# ==========================
# TO-DO LIST
# ==========================

# List to store tasks
task = []

# Function to add a task
def new_task(add_task):
    task.append(add_task)

# Function to view all tasks
def view_tasks():

    if len(task) == 0:
        print("No task added.")

    else:
        print("\n===== YOUR TASKS =====")

        for i in range(len(task)):
            print(f"{i + 1}. {task[i]}")

# Function to remove a task
def remove_task():

    if len(task) == 0:
        print("No task to remove.")

    else:
        view_tasks()

        remove = int(input("Enter the task number to remove: "))

        if remove >= 1 and remove <= len(task):
            task.pop(remove - 1)
            print("Task removed successfully.")

        else:
            print("Invalid task number.")


while True:

    print("\n===== TO-DO LIST =====")

    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    try:

        choice = int(input("Select an option: "))

        if choice == 1:

            add_task = input("Enter a task: ")

            if add_task.strip() == "":
                print("Task cannot be empty.")

            else:
                new_task(add_task)
                print("Task added successfully.")

        elif choice == 2:

            view_tasks()

        elif choice == 3:

            remove_task()

        elif choice == 4:

            print("Thank you for using the To-Do List.")
            break

        else:

            print("Enter a number from 1 to 4.")

    except ValueError:

        print("Sorry, that's an invalid input.")