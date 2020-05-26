from colorama import Fore
from gendiff.difference import REMOVED, ADDED, NON_CHANGED, CHANGED, NESTED, generate_diff
from gendiff.files import read_file

MARKERS = {
    "non_changed": None,
    "removed": "- ",
    "added": "+ ",
    "changed": None,
    "nested": None
}


def make_result(list_, spaces):
    string_spaces = " " * spaces
    result = ["{\n"]

    for (key, status, value) in list_:
        if status == NESTED:
            result.append(f"{string_spaces} {key}:{value}")

        elif status == REMOVED:
            result.append(f"{string_spaces}- {key}: {value}\n")

        elif status == ADDED:
            result.append(f"{string_spaces}+ {key}: {value}\n")

        elif status == CHANGED:
            result.append(f"{string_spaces}- {key}: {value[0]}\n")
            result.append(f"{string_spaces}+ {key}: {value[1]}\n")

        elif status == NON_CHANGED:
            result.append(f"{string_spaces}  {key}: {value}\n")
    result.append("}\n")
    return result


def render_dictionary(dictionary, spaces=2):
    strings = []
    for key, (status, value) in dictionary.items():
        if isinstance(value, dict):
            strings.append((key, status, render_dictionary(value, spaces=spaces + 4)))
        else:
            strings.append((key, status, value))

    result = (make_result(strings, spaces))
    return "".join(result)


# def check_color_condition(index, string, result, color):
#     if "{" in string[index]:
#         while "}" not in string[index]:
#             result += color + string[index] + "\n"
#             index += 1
#     return result, index


file1 = read_file("/home/tatoxa/python_projects/python-project-lvl2/tests/fixtures/test_before_2.json")
file2 = read_file("/home/tatoxa/python_projects/python-project-lvl2/tests/fixtures/test_after_2.json")
d = (generate_diff(file1, file2))
print(render_dictionary(d))
# s = render_dictionary(d)
# for elem in s:
#     print(elem, type(elem))
