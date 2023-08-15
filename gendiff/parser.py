import yaml
import json
import os.path


def parse_data(file_path: str) -> dict:
    root, ext = os.path.splitext(file_path)
    if ext == '.yml' or '.yaml':
        return yaml.safe_load(open(file_path))
    if ext == '.json':
        return json.loads(open(file_path))
    raise ValueError(f"Нераспознаваемый формат {ext}!")
