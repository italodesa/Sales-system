from pathlib import Path
import json

def verify(path):
    BASE_DIR = Path(path).resolve().parent.parent
    DATA_DIR = BASE_DIR / "data"
    DATA_FILE = DATA_DIR / path

    DATA_DIR.mkdir(exist_ok=True)

    if not DATA_FILE.exists():
        with open(DATA_FILE,"w",encoding="utf-8") as f:
            json.dump([],f)

    return DATA_FILE

def return_data(path):
    path = verify(path)
    with open(path,"r",encoding="utf-8") as f:
        data = json.load(f)
    return data

def append_file(path,your_data):
    path = verify(path)
    path_data = return_data(path)
    path_data.append(your_data)
    with open(path,"w",encoding="utf-8") as f:
        json.dump(path_data, f, indent=4, ensure_ascii=False)

def save_file(path, data):
    path = verify(path)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def generate_id(path,object_id):
    data = return_data(path)
    if data:
        last_id = max(item.get(object_id, 0) for item in data) + 1
    else:
        last_id = 1

    return last_id