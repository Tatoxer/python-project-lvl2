from colorama import Fore
from gendiff.difference import REMOVED, ADDED, CHANGED, NESTED
from gendiff.difference import generate_diff
from gendiff.files import read_file


def apply_color(string, color1=Fore.WHITE, color2=Fore.WHITE, no_colors=False):
    if not no_colors:
        result = color1 + string + color2
    else:
        result = string
    return result


def make_result(list_, spaces, no_color):
    string_spaces = " " * spaces
    result = ["{\n"]

    for (key, status, value) in list_:
        if status == NESTED:
            string = f"{string_spaces} {key}: {value}\n"
            result.append(apply_color(string, no_colors=no_color))

        elif status == REMOVED:
            string = f"{string_spaces}- {key}: {value}\n"
            result.append(apply_color(string, Fore.RED, no_colors=no_color))  # noqa: E501

        elif status == ADDED:
            string = f"{string_spaces}+ {key}: {value}\n"
            result.append(apply_color(string, Fore.GREEN, no_colors=no_color))  # noqa: E501

        elif status == CHANGED:
            string_before = f"{string_spaces}- {key}: {value[0]}\n"
            string_after = f"{string_spaces}+ {key}: {value[1]}\n"
            result.append(apply_color(string_before, Fore.RED, no_colors=no_color))  # noqa: E501
            result.append(apply_color(string_after, Fore.GREEN, no_colors=no_color))  # noqa: E501

        else:
            result.append(f"{string_spaces}  {key}: {value}\n")

    result.append(' ' * (spaces - 2) + '}')
    return result


def format_dictionary(diff, no_color=False):
    def inner(dictionary, spaces=2):
        strings = []
        for key, (status, value) in dictionary.items():
            if isinstance(value, dict):
                strings.append((key, status, inner(value, spaces=spaces + 4)))  # noqa: E501
            else:
                strings.append((key, status, value))

        strings.sort()
        result = (make_result(strings, spaces, no_color))
        return "".join(result)

    return inner(diff)


file1 = read_file("/home/tatoxa/python_projects/python-project-lvl2/tests/fixtures/test_before_2.json")
file2 = read_file("/home/tatoxa/python_projects/python-project-lvl2/tests/fixtures/test_empty.json")
d = generate_diff(file1, file2)
print(format_dictionary(d))
