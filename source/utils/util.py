import json

def jason_to_dict(file):
    with open(file, "r") as f:
        data = json.load(f)
    return data