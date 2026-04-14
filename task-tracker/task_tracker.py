# Simple Task Tracker

tasks = []

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

# Test it
add_task("Learn Python")
add_task("Learn Git")
list_tasks()
mark_done(0)
list_tasks()
