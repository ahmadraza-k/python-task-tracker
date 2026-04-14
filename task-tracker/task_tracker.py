# Simple Task Tracker

import json

tasks = []
FILE_NAME = "tasks.json"

def load_tasks():
    global tasks
    try:
        with open(FILE_NAME, "r") as f:
            tasks = json.load(f)
    except FileNotFoundError:
        tasks = []

def save_tasks():
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=2)

def add_task(task_name):
    tasks.append({"name": task_name, "done": False})
    print(f"Task added: {task_name}")
    save_tasks()


def list_tasks():
    if not tasks:
        print("No tasks yet")
        return

    for i, task in enumerate(tasks):
        status = "✓" if task["done"] else "○"
        print(f"{i}. [{status}] {task['name']}")


def mark_done(task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]["done"] = True
        print(f"Task marked done: {tasks[task_index]['name']}")
        save_tasks()
    else:
        print("Invalid task number")

def delete_task(task_index):
    if 0 <= task_index < len(tasks):
        removed = tasks.pop(task_index)
        print(f"Task deleted: {removed['name']}")
        save_tasks()
    else:
        print("Invalid task number")

def run_app():
    load_tasks()

    while True:
        print("\nTask Tracker")
        print("1. Add task")
        print("2. List tasks")
        print("3. Mark task done")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            task_name = input("Enter task name: ").strip()
            if task_name:
                add_task(task_name)
            else:
                print("Task name cannot be empty")
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            try:
                task_index = int(input("Enter task number to mark done: ").strip())
                mark_done(task_index)
            except ValueError:
                print("Please enter a valid number")
        elif choice == "4":
            try:
                task_index = int(input("Enter task number to delete: ").strip())
                delete_task(task_index)
            except ValueError:
                print("Please enter a valid number")
        elif choice == "5":
            print("Goodbye")
            break
        else:
            print("Invalid option, choose 1-5")


if __name__ == "__main__":
    run_app()