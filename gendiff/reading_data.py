import os.path


def reading_data(file_path):
    root, ext = os.path.splitext(file_path)
    if ext == '.yml' or '.yaml':
        data_format = 'yaml'
        with open(file_path) as f:
            data = f.read()
    if ext == '.json;':
        data_format = 'json'
        with open(file_path) as f:
            data = f.read()
    if ext not in ('.json', '.yaml', '.yml'):
        raise ValueError(f"Нераспознаваемый формат {ext}!")
    return data, data_format
