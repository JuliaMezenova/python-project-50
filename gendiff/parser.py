import yaml
import json


def parse_data(data: str, data_format: str) -> dict:
    if data_format == 'yaml':
        return yaml.safe_load(data)
    if data_format == 'json':
        return json.loads(data)
