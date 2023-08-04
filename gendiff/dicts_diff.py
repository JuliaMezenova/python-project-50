def low_bool_values(value):
    if isinstance(value, bool):
        result = str(value).lower()
    else:
        result = value
    return result


def dicts_diff(parsed_data1, parsed_data2):
    different = []
    sorted_keys = sorted(list(
        set(parsed_data1.keys()) | set(parsed_data2.keys()))
        )
    for key in sorted_keys:
        if key not in parsed_data1:
            different.append(f"  + {key}: {low_bool_values(parsed_data2[key])}")
        elif key not in parsed_data2:
            different.append(f"  - {key}: {low_bool_values(parsed_data1[key])}")
        elif parsed_data1[key] != parsed_data2[key]:
            different.append(f"  - {key}: {low_bool_values(parsed_data1[key])}")
            different.append(f"  + {key}: {low_bool_values(parsed_data2[key])}")
        else:
            different.append(f"    {key}: {low_bool_values(parsed_data1[key])}")
    result = '{\n' + '\n'.join(different) + '\n}\n'
    return result
