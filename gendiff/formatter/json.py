import json


def formatter_json(different: dict) -> str:
    return json.dumps(different, indent=2)
