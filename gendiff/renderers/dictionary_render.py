from colorama import Fore
from gendiff.difference import REMOVED, ADDED, NON_CHANGED, CHANGED, NESTED, generate_diff
from gendiff.files import read_file


MARKERS = {
    "non_changed": None,
    "removed": "- ",
    "added": "+ ",
    "changed": None
}


def make_result(key, value, spaces, marker=None):
    result = []
    string_spaces = "" + (" " * spaces)
    if not marker:
        marker = "  "
    result.append(f"{string_spaces}{marker} {key}: {value}\n")
    return result


def render_dictionary(dictionary, spaces=2):
    result = ["{" + "\n"]
    for key, value in dictionary.items():
        if value[0] == NESTED:
            result.extend(make_result(key, render_dictionary(value[1], spaces=spaces + 4), spaces))  # noqa: E501

        elif isinstance(value[1], dict) and not value[0] == CHANGED:  # noqa: E501
            result.extend(make_result(key, render_dictionary(value[1], spaces=spaces + 4),  # noqa: E501
                                  spaces=spaces, marker=MARKERS[value[0]]))

        elif value[0] == CHANGED:
            result.append(make_result(key, value[1][0], spaces=spaces, marker="- "))
            result.append(make_result(key, value[1][1], spaces=spaces, marker="+ "))
        else:
            result.append(make_result(key, value[1], spaces=spaces, marker=MARKERS[value[0]]))  # noqa: E501

    result.append(' ' * (spaces - 2) + '}' + "\n")
    return result


def check_color_condition(index, string, result, color):
    if "{" in string[index]:
        while "}" not in string[index]:
            result += color + string[index] + "\n"
            index += 1
    return result, index


file1 = read_file("/home/tatoxa/python_projects/python-project-lvl2/tests/fixtures/test_before_2.json")
file2 = read_file("/home/tatoxa/python_projects/python-project-lvl2/tests/fixtures/test_after_2.json")
d = (generate_diff(file1, file2))
print(render_dictionary(d))
