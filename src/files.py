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