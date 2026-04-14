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
def list_tasks():
    for i, task in enumerate(tasks):
        status = "✓" if task["done"] else "○"
        print(f"{i}. [{status}] {task['name']}")
def mark_done(task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]["done"] = True
        print(f"Task marked done: {tasks[task_index]['name']}")
    else:
        print("Invalid task number")

def delete_task(task_index):
    if 0 <= task_index < len(tasks):
        removed = tasks.pop(task_index)
        print(f"Task deleted: {removed['name']}")
        save_tasks()
    else:
        print("Invalid task number")

# Test it
load_tasks()
add_task("Learn Python")
add_task("Learn Git")
list_tasks()
mark_done(0)
list_tasks()
delete_task(1)
list_tasks()