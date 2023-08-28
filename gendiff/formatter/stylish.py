from typing import Any
from gendiff.dicts_diff import ADDED, REMOVED, HAVE_CHILDREN, UNCHANGED, UPDATED


SPACES_COUNT = 4


def stringify(value, depth: int, replacer=' ', operation_symbols='    '):
    if value is None:
        return "null"
    if isinstance(value, dict):
        lines = ['{']
        for key, val in value.items():
            if isinstance(val, dict):
                line = (f"{replacer * depth}{operation_symbols}{key}: "
                        f"{stringify(val, depth + SPACES_COUNT)}")
                lines.append(line)
            else:
                line = f"{replacer * depth}{operation_symbols}{key}: {val}"
                lines.append(line)
        lines.append(f"{replacer * depth}}}")
        return '\n'.join(lines)
    return value


def make_line(dictionary: dict, key: Any, depth: int, operation_symbols) -> str:
    return f"{' ' * depth}{operation_symbols}{dictionary['key']}: " \
        f"{stringify(dictionary[key], depth + SPACES_COUNT)}"


def formatter_stylish(different, depth=0) -> str:
    result = ['{']
    for d in different:
        operation = d['operation']
        if operation == HAVE_CHILDREN:
            new_val = formatter_stylish(d['value'], depth + SPACES_COUNT)
            result.append(f"{' ' * depth}    {d['key']}: {new_val}")
        if operation == REMOVED or operation == UPDATED:
            result.append(make_line(
                d, 'old_value', depth, operation_symbols='  - '
            ))
        if operation == ADDED or operation == UPDATED:
            result.append(make_line(
                d, 'new_value', depth, operation_symbols='  + '
            ))
        if operation == UNCHANGED:
            result.append(make_line(
                d, 'value', depth, operation_symbols='    '
            ))
    result.append(f"{' ' * depth}}}")
    return '\n'.join(result)


def stylish(different: dict) -> str:
    return formatter_stylish(different)
