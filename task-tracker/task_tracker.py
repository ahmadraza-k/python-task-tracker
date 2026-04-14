# Simple Task Tracker

tasks = []

def add_task(task_name):
    tasks.append({"name": task_name, "done": False})
    print(f"Task added: {task_name}")

# Test it
add_task("Learn Python")
add_task("Learn Git")
print(tasks)

