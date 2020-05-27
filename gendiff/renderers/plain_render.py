from colorama import Fore
from gendiff.difference import REMOVED, ADDED, CHANGED, NESTED


def make_value(value):
    if isinstance(value, dict):
        value = "complex value"
    return value


def make_result(list_):
    result = []
    for (path, status, value) in list_:
        if status == NESTED:
            result.extend(value)

        if status == REMOVED:
            result.append(f"Property {path} was {status}\n")

        elif status == ADDED:
            value = make_value(value)
            result.append(f"Property {path} was {status} with value: '{value}'\n")  # noqa: E501

        elif status == CHANGED:
            changed_value = value[1]
            changed_value = make_value(changed_value)
            result.append(f"Property {path} was {status} "
                                        f"from '{value[0]}' to '{changed_value}'\n")  # noqa: E501

    return result


def render_plain(dictionary, root_keys=None):
    strings = []

    for key, (status, value) in dictionary.items():
        path = f"{root_keys}.{key}" if root_keys else key
        if status == NESTED:
            strings.append([path, status, render_plain(value, key)])
        else:
            strings.append((path, status, value))

    result = (make_result(strings))
    return "".join(result)
