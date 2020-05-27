from colorama import Fore
from gendiff.difference import REMOVED, ADDED, NON_CHANGED, CHANGED, NESTED, generate_diff
from gendiff.files import read_file


def make_result(list_, spaces):
    string_spaces = " " * spaces
    result = ["{\n"]

    for (key, status, value) in list_:
        if status == NESTED:
            result.append(Fore.WHITE + f"{string_spaces} {key}: {value}\n")

        elif status == REMOVED:
            result.append(Fore.RED + f"{string_spaces}- {key}: {value}\n")
            result.append(Fore.WHITE + "")

        elif status == ADDED:
            result.append(Fore.GREEN + f"{string_spaces}+ {key}: {value}\n")
            result.append(Fore.WHITE + "")

        elif status == CHANGED:
            result.append(Fore.RED + f"{string_spaces}- {key}: {value[0]}\n")
            result.append(Fore.GREEN + f"{string_spaces}+ {key}: {value[1]}\n")
            result.append(Fore.WHITE + "")

        else:
            result.append(f"{string_spaces}  {key}: {value}\n")

    result.append(' ' * (spaces - 2) + '}' + "\n")
    return result


def render_dictionary(dictionary, spaces=2):
    strings = []
    for key, (status, value) in dictionary.items():
        if isinstance(value, dict):
            strings.append((key, status, render_dictionary(value, spaces=spaces + 4)))
        else:
            strings.append((key, status, value))

    result = (make_result(strings, spaces))
    #"".join(result)
    return "".join(result)


file1 = read_file("/home/tatoxa/python_projects/python-project-lvl2/tests/fixtures/test_before_2.json")
file2 = read_file("/home/tatoxa/python_projects/python-project-lvl2/tests/fixtures/test_after_2.json")
d = (generate_diff(file1, file2))
print(render_dictionary(d))

