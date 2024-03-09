
# The Daily Planner

tasks = {}

# Task 1: Add a Task
def add_task(time, task):
    tasks[time] = task
    print(f"Task '{task}' added at {time}.")

# Task 2: Remove a Task
def remove_task(time):
    if time in tasks:
        print(f"Task '{tasks.pop(time)}' removed.")
    else:
        print("No task found at that time.")

# Task 3: Display All Tasks
def display_tasks():
    for time, task in sorted(tasks.items()):
        print(f"{time}: {task}")

# Sample Function Calls
add_task("09:00", "Meeting")
add_task("12:00", "Lunch")
remove_task("09:00")
display_tasks()
