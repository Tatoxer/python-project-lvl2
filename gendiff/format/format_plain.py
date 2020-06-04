from colorama import Fore
from gendiff.format.format_dictionary import apply_color
from gendiff.difference import REMOVED, ADDED, CHANGED, NESTED


def change_value_to_complex(value):
    if isinstance(value, dict):
        value = "complex value"
    return value


def make_result(list_, no_color):
    result = []
    for (path, status, value) in list_:
        if status == NESTED:
            result.extend(value)

        if status == REMOVED:
            string = f"Property '{path}' was {status}\n"
            result.append(apply_color(string, Fore.RED, no_colors=no_color))

        elif status == ADDED:
            value = change_value_to_complex(value)
            string = f"Property '{path}' was {status} with value: '{value}'\n"
            result.append(apply_color(string, Fore.GREEN, no_colors=no_color))

        elif status == CHANGED:
            value_before, changed_value = value[0], value[1]
            value_before = change_value_to_complex(value_before)
            changed_value = change_value_to_complex(changed_value)
            string = f"Property '{path}' was {status} from " \
                     f"'{value_before}' to '{changed_value}'\n"
            result.append(apply_color(string, Fore.YELLOW, no_colors=no_color))

    return result


def format_plain(diff, no_color=False):
    def inner(dictionary, root_keys=None):
        strings = []
        for key, (status, value) in dictionary.items():
            path = f"{root_keys}.{key}" if root_keys else key
            if status == NESTED:
                strings.append([path, status, inner(value, path)])
            else:
                strings.append((path, status, value))

        strings = list(map(list, strings))
        strings.sort()
        result = (make_result(strings, no_color))
        return "".join(result)
    return inner(diff)
