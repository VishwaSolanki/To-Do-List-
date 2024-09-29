import os

# In-memory list to store tasks (use a file/database for persistence)
tasks = []

# Function to display the menu
def show_menu():
    print("\n=== To-Do List Application ===")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

# Function to add a task
def add_task():
    task = input("\nEnter the task: ")
    tasks.append({"title": task, "completed": False})
    print(f"Task '{task}' added.")

# Function to list all tasks
def list_tasks():
    if not tasks:
        print("\nNo tasks found.")
    else:
        print("\nTasks:")
        for i, task in enumerate(tasks):
            status = "✔" if task["completed"] else "✘"
            print(f"{i + 1}. {task['title']} [{status}]")

# Function to mark a task as completed
def mark_task_completed():
    list_tasks()
    if tasks:
        try:
            task_num = int(input("\nEnter task number to mark as completed: "))
            if 1 <= task_num <= len(tasks):
                tasks[task_num - 1]["completed"] = True
                print(f"Task '{tasks[task_num - 1]['title']}' marked as completed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

# Function to delete a task
def delete_task():
    list_tasks()
    if tasks:
        try:
            task_num = int(input("\nEnter task number to delete: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Task '{removed_task['title']}' deleted.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

# Main function to run the CLI-based To-Do List application
def main():
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-5): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            mark_task_completed()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("\nExiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
