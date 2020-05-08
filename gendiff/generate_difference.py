import json
import os.path


def generate_added_key(key, value):
    formatted_key = f'+ {key}'
    return {formatted_key: str(value)}


def generate_removed_key(key, value):
    formatted_key = f'- {key}'
    return {formatted_key: str(value)}


def print_keys_values(dictionary):
    for key, value in dictionary.items():
        print(f'{key}: {str(value)}')


def mark_difference(key, before, after):
    difference = {}
    if key in after and before[key] != after[key]:
        difference.update(generate_removed_key(key, before[key]))
        difference.update(generate_added_key(key, after[key]))
    return difference


def mark_removed(key, dictionary_before, dictionary_after):
    difference = {}
    if key not in dictionary_after:
        difference.update(generate_removed_key(key, dictionary_before[key]))
    return difference


def mark_added(key, dictionary_before, dictionary_after):
    difference = {}
    if key not in dictionary_before:
        difference.update(generate_added_key(key, dictionary_after[key]))
    return difference


def generate_diff(dir_1, dir_2):
    difference = {}
    dir_1 = os.path.abspath(dir_1)
    dir_2 = os.path.abspath(dir_2)

    file_1 = json.load(open(dir_1))
    file_2 = json.load(open(dir_2))

    for key, value in file_1.items():
        difference.update(mark_difference(key, file_1, file_2))
        difference.update(mark_removed(key, file_1, file_2))

    for key, value in file_2.items():
        difference.update(mark_added(key, file_1, file_2))

    print_keys_values(difference)
    return difference
