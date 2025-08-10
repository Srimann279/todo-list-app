import os

TASKS_FILE = "tasks.txt"

# ---------------------------
# Load tasks from file
# ---------------------------
def load_tasks():
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            tasks = [line.strip() for line in file]
    return tasks

# ---------------------------
# Save tasks to file
# ---------------------------
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# ---------------------------
# Display tasks
# ---------------------------
def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

# ---------------------------
# Main menu
# ---------------------------
def main():
    tasks = load_tasks()

    while True:
        print("\n===== TO-DO LIST MENU =====")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Clear all tasks")
        print("5. Save and Exit")

        choice = input("Enter choice (1-5): ").strip()

        if choice == "1":
            show_tasks(tasks)

        elif choice == "2":
            task = input("Enter new task: ").strip()
            if task:
                tasks.append(task)
                print(f"✅ Task '{task}' added.")
            else:
                print("⚠️ Task cannot be empty.")

        elif choice == "3":
            show_tasks(tasks)
            if tasks:
                try:
                    task_num = int(input("Enter task number to delete: "))
                    if 1 <= task_num <= len(tasks):
                        removed = tasks.pop(task_num - 1)
                        print(f"🗑️ Task '{removed}' deleted.")
                    else:
                        print("⚠️ Invalid task number.")
                except ValueError:
                    print("⚠️ Please enter a valid number.")

        elif choice == "4":
            confirm = input("Are you sure you want to clear all tasks? (y/n): ").lower()
            if confirm == "y":
                tasks.clear()
                print("🗑️ All tasks cleared.")

        elif choice == "5":
            save_tasks(tasks)
            print("💾 Tasks saved. Goodbye!")
            break

        else:
            print("⚠️ Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
