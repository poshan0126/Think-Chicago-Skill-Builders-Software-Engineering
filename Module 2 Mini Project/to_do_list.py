
class Task:
    def __init__(self, title, priority='Normal'):
        self.title = title
        self.is_complete = False
        self.priority = priority

class ToDoListApp:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        title = input("Enter task title: ")
        priority = input("Enter task priority (Low, Normal, High): ")
        if priority not in ['Low', 'Normal', 'High']:
            print("Invalid priority. Setting to Normal.")
            priority = 'Normal'
        self.tasks.append(Task(title, priority))
        print("Task added.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks yet.")
            return
        for index, task in enumerate(self.tasks, start=1):
            status = "Complete" if task.is_complete else "Incomplete"
            print(f"{index}. {task.title} - {status} - Priority: {task.priority}")

    def mark_task_complete(self):
        if not self.tasks:
            print("No tasks to mark as complete.")
            return
        self.view_tasks()
        try:
            task_number = int(input("Enter task number to mark as complete: "))
            self.tasks[task_number - 1].is_complete = True
            print("Task marked as complete.")
        except (ValueError, IndexError):
            print("Invalid task number.")

    def delete_task(self):
        if not self.tasks:
            print("No tasks to delete.")
            return
        self.view_tasks()
        try:
            task_number = int(input("Enter task number to delete: "))
            del self.tasks[task_number - 1]
            print("Task deleted.")
        except (ValueError, IndexError):
            print("Invalid task number.")

    def quit_app(self):
        print("Quitting the app. Goodbye!")
        exit()

    def show_menu(self):
        options = {
            "1": self.add_task,
            "2": self.view_tasks,
            "3": self.mark_task_complete,
            "4": self.delete_task,
            "5": self.quit_app,
        }
        while True:
            print("\nWelcome to the To-Do List App!\n")
            print("Menu:")
            print("1. Add a task")
            print("2. View tasks")
            print("3. Mark a task as complete")
            print("4. Delete a task")
            print("5. Quit")
            choice = input("Select an option: ")
            action = options.get(choice)
            if action:
                action()
            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    app = ToDoListApp()
    app.show_menu()
