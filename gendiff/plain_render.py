from gendiff.generate_difference import generate_diff
from gendiff.open_file import open_file

REMOVED, ADDED, NON_CHANGED, CHANGED, NESTED = (
    "removed", "added", "non_changed", "changed", "nested"
)


def make_result(key, value):
    print(value)
    string = "Property "
    if value[0] == REMOVED:
        return f"{string}'{key}' was {value[0]}\n"

    elif value[0] == CHANGED:
        return f"{string}'{key}' was {value[0]} from '{value[1]}' to '{value[2]}'\n"

    elif value[0] == ADDED:
        if isinstance(value[1], dict):
            return f"{string}'{key}' was {value[0]} with value: 'complex value'\n"
        else:
            return f"{string}'{key}' was {value[0]} with value: '{value[1]}'\n"

    else:
        return ""


def render_plain(dictionary):
    result = ""
    for key, value in dictionary.items():
        if isinstance(value[1], dict) and value[0] == REMOVED:
            a, b = REMOVED, value[1]
            result += make_result(key, (a, b))

        elif isinstance(value[1], dict) and value[0] == ADDED:
            a, b = ADDED, value[1]
            result += make_result(key, (a, b))
        elif isinstance(value[1], dict):
            result += make_result(key, render_plain(value[1]))
        else:
            result += make_result(key, value)
    return result


file_1 = open_file("/home/tatoxa/python_projects/python-project-lvl2/tests/fixtures/test_files/before_2.json")
file_2 = open_file("/home/tatoxa/python_projects/python-project-lvl2/tests/fixtures/test_files/after_2.json")
dict_ = generate_diff(file_1, file_2)
print(render_plain(dict_))
