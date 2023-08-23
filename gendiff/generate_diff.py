from gendiff.parser import parse_data
from gendiff.dicts_diff import dicts_diff
from gendiff.formatter.get_format_name import get_format_name
from gendiff.reading_data import reading_data


def generate_diff(first_file, second_file, format_name='stylish'):
    data1, data_format1 = reading_data(first_file)
    data2, data_format2 = reading_data(second_file)
    parsed_data1 = parse_data(data1, data_format1)
    parsed_data2 = parse_data(data2, data_format2)
    diff = dicts_diff(parsed_data1, parsed_data2)
    return get_format_name(format_name)(diff)
