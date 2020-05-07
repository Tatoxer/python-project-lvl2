import json
import os.path


def generate_added_key(key, value):
    formatted_key = f'+ {key}'
    return {formatted_key: value}


def generate_removed_key(key, value):
    formatted_key = f'- {key}'
    return {formatted_key: value}


def generate_diff(dir_1, dir_2):
    difference = {}
    dir_1 = os.path.abspath(dir_1)
    dir_2 = os.path.abspath(dir_2)
    
    file_1 = json.load(open(dir_1))
    file_2 = json.load(open(dir_2))

    for key, value in file_1.items():
        if key in file_2 and value != file_2[key]:
            difference.update(generate_removed_key(key, value))
            difference.update(generate_added_key(key, file_2[key]))

        if key not in file_2:
            difference.update(generate_removed_key(key, file_1[key]))

    for key, value in file_2.items():
        if key not in file_1:
            difference.update(generate_added_key(key, file_2[key]))

    for key, value in difference.items():
        print(f'{key}: {str(value)}')
