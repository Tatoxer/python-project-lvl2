from colorama import Fore, init
from gendiff.difference import REMOVED, ADDED, CHANGED, NESTED, generate_diff
from gendiff.files import read_file

init()


def make_result(list_, spaces):
    string_spaces = " " * spaces
    result = ["{\n"]

    for elem in list_:
        if len(elem) == 3:
            key = elem[0]
            status = elem[1]
            value = elem[2]
            if status == NESTED:
                result.append(f"{string_spaces} {key}: {value}\n")

            elif status == REMOVED:
                result.append(f"{string_spaces}- {key}: {value}\n")
                # result.append(Fore.WHITE + "")

            elif status == ADDED:
                result.append(f"{string_spaces}+ {key}: {value}\n")
                # result.append(Fore.WHITE + "")

            elif status == CHANGED:
                result.append(f"{string_spaces}- {key}: {value[0]}\n")
                result.append(f"{string_spaces}+ {key}: {value[1]}\n")
                # result.append(Fore.WHITE + "")

            else:
                result.append(f"{string_spaces}  {key}: {value}\n")
        else:
            result.append(f"{string_spaces} {elem[0]}: {elem[1]}\n")

    result.append(' ' * (spaces - 2) + '}')
    return result


def render_dictionary(dictionary, spaces=2):
    strings = []
    for key, value in dictionary.items():
        if isinstance(value, bool):
            value = str(value)
        if len(value) == 2:
            status = value[0]
            value = value[1]
            if isinstance(value, dict):
                strings.append((key, status, render_dictionary(value, spaces=spaces + 4)))  # noqa: E501
            else:
                strings.append((key, status, value))
        else:
            if isinstance(value, dict):
                strings.append((key, render_dictionary(value, spaces=spaces + 4)))
            else:
                strings.append((key, value))

    strings.sort()
    result = (make_result(strings, spaces))
    #print(result)
    # "".join(result)
    return "".join(result)


file1 = read_file("/home/tatoxa/python_projects/python-project-lvl2/tests/fixtures/test_before_2.json")
file2 = read_file("/home/tatoxa/python_projects/python-project-lvl2/tests/fixtures/test_empty.json")
d = generate_diff(file1, file2)
# # print(file2)
#print(d)
print(render_dictionary(d))
