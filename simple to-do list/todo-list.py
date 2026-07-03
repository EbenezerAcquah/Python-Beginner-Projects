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
