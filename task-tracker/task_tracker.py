# Simple Task Tracker

tasks = []

def add_task(task_name):
    tasks.append({"name": task_name, "done": False})
    print(f"Task added: {task_name}")
def list_tasks():
    for i, task in enumerate(tasks):
        status = "✓" if task["done"] else "○"
        print(f"{i}. [{status}] {task['name']}")

# Test it
add_task("Learn Python")
add_task("Learn Git")
print(tasks)

