import yaml
import json


def parse_data(data: str, data_format: str) -> dict:
    parsers = {
        "yaml": yaml.safe_load,
        "yml": yaml.safe_load,
        "json": json.loads
    }
    return parsers[data_format](data)
