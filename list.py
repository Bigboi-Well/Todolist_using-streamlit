
import json
import os
TASKS_FILE = 'tasks.json'
def load_tasks():
    """Load tasks from a JSON file."""
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as file:
        return json.load(file)
def save_tasks(tasks):
    """Save tasks to a JSON file."""
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=2)
def show_tasks(tasks):
    """Display all tasks with their status."""
    if not tasks:
        print("No tasks found.")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, 1):
        status = "✔" if task["done"] else "✘"
        print(f"{i}. [{status}] {task['title']}")
    print()
def add_task(tasks):
    """Add a new task."""
    title = input("Enter task title: ").strip()
    if title:
        tasks.append({"title": title, "done": False})
        print("Task added.")
    else:
        print("Task title cannot be empty.")
