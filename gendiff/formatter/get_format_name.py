from gendiff.formatter.plain import plain
from gendiff.formatter.stylish import stylish


def get_format_name(format_name):
    if format_name == 'plain':
        return plain
    if format_name == 'stylish':
        return stylish
