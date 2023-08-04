import json


def parse_data(file_path):
    return json.load(open(file_path))
