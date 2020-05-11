from collections import OrderedDict


def generate_added_key(key, value):
    formatted_key = f'+ {key}'
    return {formatted_key: value}


def generate_removed_key(key, value):
    formatted_key = f'- {key}'
    return {formatted_key: value}


def print_keys_values(dictionary):
    for key, value in dictionary.items():
        print(f'{key}: {value}')


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


def mark_non_changed(key, dictionary_before, dictionary_after):
    difference = {}
    if key in dictionary_after and dictionary_before[key] == dictionary_after[key]:
        difference.update({key: dictionary_before[key]})
    return difference


difference = OrderedDict()


def generate_diff(before, after):
    for key, value in before.items():
        if isinstance(value, (dict, list)):
            if key not in after:
                difference.update(generate_removed_key(key, before[key]))
                continue
            generate_diff(value, after[key])
        else:
            difference.update(mark_difference(key, before, after))
            difference.update(mark_non_changed(key, before, after))

    for key, value in after.items():
        if isinstance(value, (dict, list)):
            if key not in before:
                difference.update(mark_added(key, before, after))
                continue

    return difference




