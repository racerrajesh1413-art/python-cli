"""A simple beginner-friendly to-do list CLI."""


def show_menu():
    print("\n=== To-Do List ===")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Exit")


def view_tasks(tasks):
    if not tasks:
        print("No tasks yet. Add one!")
        return

    print("\nYour tasks:")
    for index, task in enumerate(tasks, start=1):
        status = "[x]" if task["done"] else "[ ]"
        print(f"{index}. {status} {task['name']}")


def add_task(tasks):
    name = input("Enter a task: ").strip()
    if not name:
        print("Task cannot be empty.")
        return

    tasks.append({"name": name, "done": False})
    print(f"Task added: {name}")


def complete_task(tasks):
    if not tasks:
        print("There are no tasks to complete.")
        return

    view_tasks(tasks)
    try:
        choice = int(input("Enter the task number to complete: ")) - 1
        if 0 <= choice < len(tasks):
            tasks[choice]["done"] = True
            print(f"Completed: {tasks[choice]['name']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def delete_task(tasks):
    if not tasks:
        print("There are no tasks to delete.")
        return

    view_tasks(tasks)
    try:
        choice = int(input("Enter the task number to delete: ")) - 1
        if 0 <= choice < len(tasks):
            deleted = tasks.pop(choice)
            print(f"Deleted: {deleted['name']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    tasks = []
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
