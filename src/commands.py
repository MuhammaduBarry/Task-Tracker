from datetime import datetime

from task import task
from os_handle import load_json, dump_json

file = "./data.json"
status = ["todo", "in-progress", "done"]

def add(args: str):
    data = load_json(file)
    num_task = data.get("num_of_task", 0) + 1
    data["num_of_task"] = num_task

    current_time = datetime.now().strftime("%dT%H:%M:%SZ")

    new_task = task(num_task, 
                    args,
                    status[0],
                    current_time,
                    None)
    data["tasks"].append(new_task)

    return dump_json(file, data)

def update(args: str):
    pass

def delete(args: str):
    pass

def mark_in_progress(args: str):
    pass

def update(args: str):
    pass

def list(args: str):
    pass