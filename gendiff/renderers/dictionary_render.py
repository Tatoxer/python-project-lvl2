from colorama import Fore
from gendiff.difference import CHANGED, NESTED


MARKERS = {
    "non_changed": None,
    "removed": "- ",
    "added": "+ ",
    "changed": None
}


def make_result(key, value, spaces, marker=None):
    string_spaces = "" + (" " * spaces)
    if not marker:
        marker = "  "
    return f"{string_spaces}{marker} {key}: {value}\n"


def render_dictionary(dictionary, spaces=2):
    result = "{" + "\n"
    for key, value in dictionary.items():
        if value[0] == NESTED:
            result += make_result(key, render_dictionary(value[1], spaces=spaces + 4), spaces)  # noqa: E501

        elif isinstance(value[1], dict) and not value[0] == CHANGED:  # noqa: E501
            result += make_result(key, render_dictionary(value[1], spaces=spaces + 4),  # noqa: E501
                                  spaces=spaces, marker=MARKERS[value[0]])

        elif value[0] == CHANGED:
            result += make_result(key, value[2], spaces=spaces, marker="- ")
            result += make_result(key, value[1], spaces=spaces, marker="+ ")
        else:
            result += make_result(key, value[1], spaces=spaces, marker=MARKERS[value[0]])  # noqa: E501

    result += ' ' * (spaces - 2) + '}' + "\n"
    #print_colored_dict(result)
    return result


def check_color_condition(index, string, result, color):
    if "{" in string[index]:
        while "}" not in string[index]:
            result += color + string[index] + "\n"
            index += 1
    return result, index


def print_colored_dict(string):
    result = ""
    string = string.splitlines()
    index = 0
    while index < len(string):
        if "-" in string[index]:
            result, index = check_color_condition(index, string, result, Fore.RED)  # noqa: E501
            result += Fore.RED + string[index] + "\n"
            index += 1

        elif "+" in string[index]:
            result, index = check_color_condition(index, string, result, Fore.GREEN)    # noqa: E501
            result += Fore.GREEN + string[index] + "\n"
            index += 1
        else:
            result += Fore.WHITE + string[index] + "\n"
            index += 1
    print(result)
