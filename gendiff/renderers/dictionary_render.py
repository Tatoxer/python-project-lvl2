from colorama import Fore, init
from gendiff.difference import REMOVED, ADDED, CHANGED, NESTED, generate_diff
from gendiff.files import read_file

init()


def make_result(list_, spaces):
    string_spaces = " " * spaces
    result = ["{\n"]

    for (key, status, value) in list_:
        if status == NESTED:
            result.append(f"{string_spaces} {key}: {value}\n")

        elif status == REMOVED:
            result.append(f"{string_spaces}- {key}: {value}\n")
            #result.append(Fore.WHITE + "")

        elif status == ADDED:
            result.append(f"{string_spaces}+ {key}: {value}\n")
            #result.append(Fore.WHITE + "")

        elif status == CHANGED:
            result.append(f"{string_spaces}- {key}: {value[0]}\n")
            result.append(f"{string_spaces}+ {key}: {value[1]}\n")
            #result.append(Fore.WHITE + "")

        else:
            result.append(f"{string_spaces}  {key}: {value}\n")

    result.append(' ' * (spaces - 2) + '}' + "\n")
    return result


def render_dictionary(dictionary, spaces=2):
    strings = []
    for key, (status, value) in dictionary.items():
        if isinstance(value, dict):
            strings.append((key, status, render_dictionary(value, spaces=spaces + 4)))  # noqa: E501
        else:
            strings.append((key, status, value))

    result = (make_result(strings, spaces))
    #"".join(result)
    return "".join(result)


file1 = read_file("/home/tatoxa/python_projects/python-project-lvl2/tests/fixtures/test_empty.json")
file2 = read_file("/home/tatoxa/python_projects/python-project-lvl2/tests/fixtures/test_before_2.json")
d = generate_diff(file1, file2)
print(d)
# print(render_dictionary(d))
