from gendiff.parser import parse_data
from gendiff.dicts_diff import dicts_diff
from gendiff.formatter.stylish import stylish


def generate_diff(first_file, second_file, format='stylish'):
    parsed_data1 = parse_data(first_file)
    parsed_data2 = parse_data(second_file)
    diff = dicts_diff(parsed_data1, parsed_data2)
    return stylish(diff)
