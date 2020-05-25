from colorama import Fore
from gendiff.difference import REMOVED, ADDED, CHANGED, NESTED
from gendiff.files import read_file
from gendiff.difference import generate_diff


def make_result(key, status, value):
    if status == REMOVED:
        result = Fore.RED + f"Property '{key}' was {status}\n"

    elif status == CHANGED:
        if isinstance(value[1][1], dict):
            result = Fore.YELLOW + f"Property '{key}' was {status} " \
                                   f"from '{value[0]}' to 'complex value'\n"
        else:
            result = Fore.YELLOW + f"Property '{key}' was {status} " \
                                   f"from '{value[0]}' to '{value[1]}'\n"

    elif status == ADDED:
        if isinstance(value, dict):
            result = Fore.GREEN + f"Property '{key}' was {status} " \
                                  f"with value: 'complex value'\n"
        else:
            result = Fore.GREEN + f"Property '{key}' was {status} " \
                                  f"with value: '{value}'\n"

    else:
        result = ""

    return result


def render_plain(dictionary):
    result = ""

    for key, (status, value) in dictionary.items():
        path = key
        if status == REMOVED:
            result += make_result(path, status, value)

        elif status == ADDED:
            result += make_result(path, status, value)

        elif isinstance(value, dict):
            result += render_plain(value)
        else:
            result += make_result(path, status, value)
    return result


def build_path(dictionary, root_keys=None):
    result = ""
    for key, (status, value) in dictionary.items():
        path = f"{root_keys}.{key}" if root_keys else key
        if isinstance(value, dict):
            build_path(value, path)
        else:
            result = path
    print(result)
    return result


file1 = read_file("/home/tatoxa/python_projects/python-project-lvl2/tests/fixtures/test_before_2.json")
file2 = read_file("/home/tatoxa/python_projects/python-project-lvl2/tests/fixtures/test_after_2.json")
d = generate_diff(file1, file2)
#print(render_plain(d))
print(build_path(d))
