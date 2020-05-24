from colorama import Fore
from gendiff.difference import REMOVED, ADDED, CHANGED


def make_result(key, value):
    if value[0] == REMOVED:
        result = Fore.RED + f"Property '{key}' was {value[0]}\n"

    elif value[0] == CHANGED:
        if isinstance(value[1][1], dict):
            result = Fore.YELLOW + f"Property '{key}' was {value[0]} " \
                     f"from '{value[1][0]}' to 'complex value'\n"
        else:
            result = Fore.YELLOW + f"Property '{key}' was {value[0]} " \
                     f"from '{value[1][0]}' to '{value[1][1]}'\n"

    elif value[0] == ADDED:
        if isinstance(value[1], dict):
            result = Fore.GREEN + f"Property '{key}' was {value[0]} " \
                     f"with value: 'complex value'\n"
        else:
            result = Fore.GREEN + f"Property '{key}' was {value[0]} " \
                     f"with value: '{value[1]}'\n"

    else:
        result = ""

    return result


def render_plain(dictionary, root_keys=None):
    result = ""

    for key, value in dictionary.items():
        path = f"{root_keys}.{key}" if root_keys else key
        if isinstance(value[1], dict) and value[0] == REMOVED:
            value_1, value_2 = REMOVED, value[1]
            result += make_result(path, (value_1, value_2))

        elif isinstance(value[1], dict) and value[0] == ADDED:
            value_1, value_2 = ADDED, value[1]
            result += make_result(path, (value_1, value_2))

        elif isinstance(value[1], dict):
            result += render_plain(value[1], path)

        else:
            result += make_result(path, value)
    return result



