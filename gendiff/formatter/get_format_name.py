from gendiff.formatter.plain import plain
from gendiff.formatter.stylish import stylish
from gendiff.formatter.json import formatter_json


def get_format_name(format_name):
    if format_name == 'plain':
        return plain
    if format_name == 'stylish':
        return stylish
    if format_name == 'json':
        return formatter_json
