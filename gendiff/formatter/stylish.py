import itertools
from typing import Any


SPACES_COUNT = 4
def stringify(value, depth: int, replacer=' ', operation_symbols='    '):
    if isinstance(value, bool):
        return str(value)
    if isinstance(value, int):
        return value
    if isinstance(value, dict):
        lines = ['{']
        for key, val in value.items():
            if not isinstance(val, dict):
                line = f"{replacer * depth}{operation_symbols}{key}: {val}"
                lines.append(line)
            if isinstance(val, dict):
                line = f"{replacer * depth}{operation_symbols}{key}: " + '{'
                lines.append(line)
                stringify(val, depth + SPACES_COUNT)
                lines.append(f"replacer * (depth + SPACES_COUNT)" + '}')
        result = itertools.chain(lines + '}')
        return '\n'.join(result)
        
            
def formatter_stylish(different: dict, depth=0):
    result = ['{']
    for d in different:
        new_d = dict({d['key']: d['value']})
        if d['operation'] == 'added':
            result.append(stringify(new_d, depth, replacer=' ', operation_symbols='  + '))
        if d['operation'] == 'deleted':
            result.append(stringify(new_d, depth, replacer=' ', operation_symbols='  - '))
        if d['operation'] == 'unchanged':
            result.append(stringify(new_d, depth, replacer=' ', operation_symbols='    '))
        if d['operation'] == 'have_children':
            new_val = formatter_stylish(new_d, depth + SPACES_COUNT)
            result.append(f"{' ' * depth}    {key}: {new_val}")
    result.append('}')
    return '\n'.join(result)


def stylish(different: dict) -> str:
    return formatter_stylish(different)
