from colorama import Fore
from gendiff.difference import REMOVED, ADDED, CHANGED, NESTED
from gendiff.files import read_file
from gendiff import generate_diff


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
            result.append(Fore.RED + f"Property {path} was {status}\n")

        elif status == ADDED:
            value = make_value(value)
            result.append(Fore.GREEN + f"Property {path} was {status} with value: '{value}'\n")

        elif status == CHANGED:
            changed_value = value[1]
            changed_value = make_value(changed_value)
            result.append(Fore.YELLOW + f"Property {path} was {status} "
                                        f"from '{value[0]}' to '{changed_value}'\n")

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
    #"".join(result)
    return strings



# file1 = read_file("/home/tatoxa/python_projects/python-project-lvl2/tests/fixtures/test_before_2.json")
# file2 = read_file("/home/tatoxa/python_projects/python-project-lvl2/tests/fixtures/test_after_2.json")
# d = (generate_diff(file1, file2))
# print(render_plain(d))
