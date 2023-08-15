def low_bool_values(value):
    if isinstance(value, bool):
        result = str(value).lower()
    else:
        result = value
    return result


def dicts_diff(parsed_data1: dict, parsed_data2: dict):
    different = []
    sorted_keys = sorted(
        list(set(parsed_data1.keys()) | set(parsed_data2.keys()))
        )
    for key in sorted_keys:
        if key not in parsed_data1:
            different.append({
                'key': key,
                'value': low_bool_values(parsed_data2[key]),
                'operation': 'added'
                })
        elif key not in parsed_data2:
            different.append({
                'key': key,
                'value': low_bool_values(parsed_data1[key]),
                'operation': 'deleted'
                })
        elif isinstance(parsed_data1[key], dict) and isinstance(parsed_data2[key], dict):
            child = dicts_diff(parsed_data1[key], parsed_data2[key])
            different.append({
                'key':key,
                'value': child,
                'operation': 'have_children'
                })
        elif parsed_data1[key] != parsed_data2[key]:
            different.append({
                'key': key,
                'value': low_bool_values(parsed_data1[key]),
                'operation': 'deleted'
                })
            different.append({
                'key': key,
                'value': low_bool_values(parsed_data2[key]),
                'operation': 'added'
                })
        elif parsed_data1[key] == parsed_data2[key]:
            different.append({
                'key': key,
                'value': parsed_data1[key],
                'operation': 'unchanged'
                })
        
    return different
