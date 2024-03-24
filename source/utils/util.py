from pathlib import Path
import json

#root directory path where data folder is located
ROOT_DIR = Path(__file__).resolve().parent.parent
#name of data folder
DATA_FOLDER = 'data'

def jason_to_dict(file):
    data_file = ROOT_DIR.joinpath(DATA_FOLDER).joinpath(file)
    with open(data_file, "r") as f:
        data = json.load(f)
    return data