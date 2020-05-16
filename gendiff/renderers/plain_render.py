from gendiff.generate_difference import generate_diff
from gendiff.open_file import open_file

REMOVED, ADDED, NON_CHANGED, CHANGED, NESTED = (
    "removed", "added", "non_changed", "changed", "nested"
)


def make_result(key, value):
    if value[0] == REMOVED:
        result = f"Property '{key}' was {value[0]}\n"

    elif value[0] == CHANGED:
        if isinstance(value[2], dict):
            result = f"Property '{key}' was {value[0]} from '{value[1]}' to 'complex value'\n"
        else:
            result = f"Property '{key}' was {value[0]} from '{value[1]}' to '{value[2]}'\n"

    elif value[0] == ADDED:
        if isinstance(value[1], dict):
            result = f"Property '{key}' was {value[0]} with value: 'complex value'\n"
        else:
            result = f"Property '{key}' was {value[0]} with value: '{value[1]}'\n"

    else:
        result = ""
    return result


def render_plain(dictionary, root_keys=None):
    result = ""

    for key, value in dictionary.items():
        path = f"{root_keys}.{key}" if root_keys else key
        if isinstance(value[1], dict) and value[0] == REMOVED:
            value_1, value_2 = REMOVED, value[1]
            result += make_result(path, (value_1, value_2))

        elif isinstance(value[1], dict) and value[0] == ADDED:
            value_1, value_2 = ADDED, value[1]
            result += make_result(path, (value_1, value_2))

        elif isinstance(value[1], dict):
            result += render_plain(value[1], path)

        else:
            result += make_result(path, value)
    return result


file_1 = open_file("/home/tatoxa/python_projects/python-project-lvl2/tests/fixtures/test_files/before_3.json")
file_2 = open_file("/home/tatoxa/python_projects/python-project-lvl2/tests/fixtures/test_files/before_2.json")
d = generate_diff(file_1, file_2)
print(render_plain(d))