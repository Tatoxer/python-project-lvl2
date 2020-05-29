from colorama import Fore
from gendiff.difference import REMOVED, ADDED, CHANGED, NESTED


def apply_color(string, color1=Fore.WHITE, color2=Fore.WHITE, no_colors=False):
    if not no_colors:
        result = color1 + string + color2
    else:
        result = string
    return result


def make_result(list_, spaces, no_color):
    string_spaces = " " * spaces
    result = ["{\n"]

    for elem in list_:
        if len(elem) == 3:
            key = elem[0]
            status = elem[1]
            value = elem[2]
            if status == NESTED:
                string = f"{string_spaces} {key}: {value}\n"
                result.append(apply_color(string, no_colors=no_color))

            elif status == REMOVED:
                string = f"{string_spaces}- {key}: {value}\n"
                result.append(apply_color(string, Fore.RED, no_colors=no_color))

            elif status == ADDED:
                string = f"{string_spaces}+ {key}: {value}\n"
                result.append(apply_color(string, Fore.GREEN, no_colors=no_color))

            elif status == CHANGED:
                string_before = f"{string_spaces}- {key}: {value[0]}\n"
                string_after = f"{string_spaces}+ {key}: {value[1]}\n"
                result.append(apply_color(string_before, Fore.RED, no_colors=no_color))
                result.append(apply_color(string_after, Fore.GREEN, no_colors=no_color))

            else:
                result.append(f"{string_spaces}  {key}: {value}\n")
        else:
            result.append(f"{string_spaces} {elem[0]}: {elem[1]}\n")

    result.append(' ' * (spaces - 2) + '}')
    return result


def render_dictionary(diff, no_color=False):
    def inner(dictionary, spaces=2):
        strings = []
        for key, value in dictionary.items():
            if isinstance(value, bool):
                value = str(value)
            if len(value) == 2:
                status = value[0]
                value = value[1]
                if isinstance(value, dict):
                    strings.append((key, status, inner(value, spaces=spaces + 4)))  # noqa: E501
                else:
                    strings.append((key, status, value))
            else:
                if isinstance(value, dict):
                    strings.append((key, inner(value, spaces=spaces + 4)))  # noqa: E501
                else:
                    strings.append((key, value))

        strings.sort()
        result = (make_result(strings, spaces, no_color))
        return "".join(result)
    return inner(diff)
