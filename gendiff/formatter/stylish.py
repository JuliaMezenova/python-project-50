import itertools
from typing import Any


SPACES_COUNT = 4
def stringify(value, depth: int, replacer=' ', operation_symbols='    '):
    if isinstance(value, dict):
        lines = []
        for key, val in value.items():
            if isinstance(val, dict):
                line = f"{replacer * depth}{operation_symbols}{key}: " + '{'
                lines.append(line)
                lines.append(stringify(val, depth + SPACES_COUNT))
                lines.append(f"{replacer * (depth + SPACES_COUNT)}" + '}')
            if not isinstance(val, dict):
                line = f"{replacer * depth}{operation_symbols}{key}: {val}"
                lines.append(line)
        return '\n'.join(lines)
    if value is None:
        return "null"
    return value
        
            
def formatter_stylish(different, depth=0):
    result = ['{']
    for d in different:
        new_d = {}
        new_d[d.get('key')] = d.get('value')
        if d['operation'] == 'have_children':
            new_val = formatter_stylish(d.get('value'), depth + SPACES_COUNT)
            result.append(f"{' ' * depth}    {d.get('key')}: {new_val}")
        if d['operation'] == 'added':
            result.append(stringify(new_d, depth, replacer=' ', operation_symbols='  + '))
        if d['operation'] == 'deleted':
            result.append(stringify(new_d, depth, replacer=' ', operation_symbols='  - '))
        if d['operation'] == 'unchanged':
            result.append(stringify(new_d, depth, replacer=' ', operation_symbols='    '))
    result.append(f"{' ' * depth}}}")
    return '\n'.join(result)


def stylish(different: dict) -> str:
    return formatter_stylish(different)
