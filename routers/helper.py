import json
from fastapi import HTTPException

# Reading from JSON
def read_json(filepath: str):
    try:
        with open(filepath, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Invalid JSON format in file.")
    
# Writing JSON
def write_json(filepath: str, data: dict | list):
    try:
        with open(filepath, "w") as file:
            json.dump(data, file, indent=4)
    except json.JSONEncoder as e:
        return f'Error occured: {e}'