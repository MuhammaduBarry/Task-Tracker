from datetime import datetime
import sys

from task import task
from os_handle import load_json, dump_json

file = "./data.json"
status = ["todo", "in-progress", "done"]
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def add(args: str):
    # Load data
    data = load_json(file)
    num_task = data.get("num_of_task", 0) + 1
    data["num_of_task"] = num_task

    # Create a new task
    new_task = task(num_task, 
                    args,
                    status[0],
                    now,
                    None)
    data["tasks"].append(new_task)

    # Returns data to JSON file 
    return dump_json(file, data)

def update(id_arg: int, description_arg: str):
    data = load_json(file)

    if type(id_arg) == int and type(description_arg) == str:
        for task in data["tasks"]:
            if task["id"] == id_arg:
                task["description"] = description_arg
                task["updatedAt"] = now
                break # Stop loop once condition is met
            else:
                print("Task does not exist!")
    else:
        print("Wrong types!!!!")
        sys.exit(1) # Forces them out of program
    
    return dump_json(file, data)

def delete(args: int):
    data = load_json(file)

    for task in data["tasks"]:
        if task["id"] == args:
            data["tasks"].remove(task)
            data["num_of_task"] -= 1
            print(f"Task ID: {args} has been deleted on {now}")
            break
        else:
            print("Task does not exist! to create one use the add command")
    
    return dump_json(file, data)

def mark_in_progress(args: str):
    data = load_json(file)

    for task in data["tasks"]:
        if task["id"] == args:
            if task["status"] == status[1]:
                print(f"Task id: {task["id"]} status is already in-progress")
            else:
                task["status"] = status[1]
            break
    if args > data["num_of_task"]:
        print(f"Task id: {args} does not exist yet, please create one")

    return dump_json(file, data)

def mark_done(args: str):
    data = load_json(file)

    for task in data["tasks"]:
        if task["id"] == args:
            if task["status"] == status[2]:
                print(f"Task id: {task["id"]} status is already done")
            else:
                task["status"] = status[2]
            break
    if args > data["num_of_task"]:
        print(f"Task id: {args} does not exist yet, please create one")

    return dump_json(file, data)

def list_task(args: str):
    data = load_json(file)

    for task in data["tasks"]:
        if task["status"] == args:
            print(f"\n{task}\n")
            break
        else:
            print("status does not exist")
            break # I was lazy :(

def list_all_task():
    data = load_json(file)

    for task in data["tasks"]:
        print(f"\n{task}\n")