tasks = []


def show_menu():
    print("\n===== TO-DO LIST TRACKER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")


def add_task():
    task = input("Enter task: ")
    tasks.append({"task": task, "done": False})
    print("Task added successfully!")


def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["done"] else "✗"
        print(f"{index}. {task['task']} [{status}]")


def complete_task():
    view_tasks()

    if not tasks:
        return

    task_num = int(input("Enter task number: "))

    if 1 <= task_num <= len(tasks):
        tasks[task_num - 1]["done"] = True
        print("Task completed!")
    else:
        print("Invalid task number")


def delete_task():
    view_tasks()

    if not tasks:
        return

    task_num = int(input("Enter task number to delete: "))

    if 1 <= task_num <= len(tasks):
        removed = tasks.pop(task_num - 1)
        print("Deleted:", removed["task"])
    else:
        print("Invalid task number")


while True:
    show_menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        complete_task()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")