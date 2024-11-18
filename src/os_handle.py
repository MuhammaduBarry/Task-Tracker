import json

def load_json(file_name: str):
    with open(file_name, "r") as file:
        data = json.load(file)
    
    return data

def dump_json(file_name: str, data: str):
    with open(file_name, "w") as file:
        return json.dump(data, file, indent=4)