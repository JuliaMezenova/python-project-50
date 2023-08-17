def stringify(value):
    if value is None:
        return "null"
    if isinstance(value, int):
        return value
    if value in ['false', 'true']:
        return value
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, str):
        return f"'{value}'"


def output_result(different: dict, path='') -> str:
    result = []
    for d in different:
        path_to_val = f"{path}{d['key']}"
        if d['operation'] == 'added':
            line = (f"Property '{path_to_val}' was {d['operation']} with "
                    f"value: {stringify(d['new_value'])}")
            result.append(line)
        if d['operation'] == 'removed':
            line = f"Property '{path_to_val}' was removed"
            result.append(line)
        if d['operation'] == 'updated':
            line = (f"Property '{path_to_val}' was updated. "
                    f"From {stringify(d['old_value'])} to "
                    f"{stringify(d['new_value'])}")
            result.append(line)
        if d['operation'] == 'have_children':
            line = output_result(d['value'], f"{path_to_val}.")
            result.append(f"{line}")
        else:  # if d['operation'] == 'unchanged'
            pass
    return '\n'.join(result)


def plain(different: dict) -> str:
    return output_result(different)
