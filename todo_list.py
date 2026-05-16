import json
import os

FILE = "todos.json"

def load_todos():
    """Load todos from file. Return empty list if file missing or broken."""
    if not os.path.exists(FILE):
        return []
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        print("Warning: file is corrupted. Starting fresh.")
        return []

def save_todos(todos):
    """Save todos to file."""
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(todos, f, indent=2, ensure_ascii=False)

todos = load_todos()

while True:
    action = input("\n1.View  2.Add  3.Complete  4.Exit\n").strip()

    if action == "1":
        if not todos:
            print("No todos yet.")
        else:
            for i, t in enumerate(todos, 1):
                mark = "[x]" if t["done"] else "[ ]"
                print(f"{i}. {mark} {t['task']}")

    elif action == "2":
        task = input("New todo: ").strip()
        if task:
            todos.append({"task": task, "done": False})
            save_todos(todos)
            print("Added.")

    elif action == "3":
        try:
            idx = int(input("Which number to complete? ")) - 1
            todos[idx]["done"] = True
            save_todos(todos)
            print("Marked as done.")
        except (ValueError, IndexError):
            print("Invalid number.")

    elif action == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid input. Please enter 1-4.")