ADDED = 'added'
REMOVED = 'removed'
HAVE_CHILDREN = 'have_children'
UNCHANGED = 'unchanged'
UPDATED = 'updated'


def low_bool_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    return value


def dicts_diff(parsed_data1, parsed_data2):
    different = []
    sorted_keys = sorted(
        list(set(parsed_data1.keys()) | set(parsed_data2.keys()))
    )
    for key in sorted_keys:
        if key not in parsed_data1:
            different.append({
                'key': key,
                'new_value': low_bool_value(parsed_data2[key]),
                'operation': ADDED
            })
        elif key not in parsed_data2:
            different.append({
                'key': key,
                'old_value': low_bool_value(parsed_data1[key]),
                'operation': REMOVED
            })
        elif isinstance(parsed_data1[key], dict) and isinstance(
                parsed_data2[key], dict):
            child = dicts_diff(parsed_data1[key], parsed_data2[key])
            different.append({
                'key': key,
                'value': child,
                'operation': HAVE_CHILDREN
            })
        elif parsed_data1[key] != parsed_data2[key]:
            different.append({
                'key': key,
                'old_value': low_bool_value(parsed_data1[key]),
                'new_value': low_bool_value(parsed_data2[key]),
                'operation': UPDATED
            })
        else:  # if parsed_data1[key] == parsed_data2[key]:
            different.append({
                'key': key,
                'value': low_bool_value(parsed_data1[key]),
                'operation': UNCHANGED
            })
    return different
