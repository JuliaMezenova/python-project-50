import os.path


def reading_data(file_path):
    root, ext = os.path.splitext(file_path)
    if ext not in ('.json', '.yaml', '.yml'):
        raise ValueError(f"Нераспознаваемый формат {ext}!")
    data_format = ext[1:]
    with open(file_path) as f:
        data = f.read()
    return data, data_format
