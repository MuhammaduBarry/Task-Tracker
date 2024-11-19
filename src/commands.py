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
    pass

def mark_done(args: str):
    pass

def list_task(args: str):
    print(args)