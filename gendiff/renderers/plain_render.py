# from colorama import Fore
from gendiff.difference import REMOVED, ADDED, CHANGED, NESTED


def change_value_to_complex(value):
    if isinstance(value, dict):
        value = "complex value"
    return value


def make_result(list_):
    result = []
    for (path, status, value) in list_:
        if status == NESTED:
            result.extend(value)

        if status == REMOVED:
            result.append(f"Property '{path}' was {status}\n")

        elif status == ADDED:
            value = change_value_to_complex(value)
            result.append(f"Property '{path}' was {status} with value: '{value}'\n")  # noqa: E501

        elif status == CHANGED:
            value_before, changed_value = value[0], value[1]
            value_before = change_value_to_complex(value_before)
            changed_value = change_value_to_complex(changed_value)
            result.append(f"Property '{path}' was {status} "
                          f"from '{value_before}' to '{changed_value}'\n")  # noqa: E501

    return result


def render_plain(dictionary, root_keys=None):
    strings = []

    for key, (status, value) in dictionary.items():
        path = f"{root_keys}.{key}" if root_keys else key
        if status == NESTED:
            strings.append([path, status, render_plain(value, path)])
        else:
            strings.append((path, status, value))

    strings = list(map(list, strings))
    strings.sort()
    result = (make_result(strings))
    return "".join(result)
