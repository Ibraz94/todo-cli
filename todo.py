import click
import json
import os


TODO_FILE = "todo.json"

def load_tasks():
    if os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

@click.group()
def cli():
    """Simple Todo List Manager"""
    pass

@click.command()
@click.argument("task")
def add(task):
    """Add a new task to the list"""
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    click.echo(f"Task added successfully: {task}")


@click.command()
def list():
    """List all tasks in the list"""
    tasks = load_tasks()
    if not tasks:
        click.echo("No tasks in the list.")
        return
    for index, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "❌"
        click.echo(f"{index}. [{status}] {task['task']}")





@click.command()
@click.argument("task_index", type=int)
def remove(task_index):
    """Remove a task from the list"""
    tasks = load_tasks()
    if 1 <= task_index <= len(tasks):
        removed_task = tasks.pop(task_index - 1)
        save_tasks(tasks)
        click.echo(f"Task '{removed_task}' removed from the list.")
    else:
        click.echo("Invalid task index.")


cli.add_command(add)
cli.add_command(list)
cli.add_command(remove)



if __name__ == "__main__":
    cli()
