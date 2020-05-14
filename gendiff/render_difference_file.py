import json
import yaml
from gendiff.generate_difference import generate_diff
from gendiff.open_file import open_file

REMOVED, ADDED, NON_CHANGED, CHANGED, NESTED = (
    "removed", "added", "non_changed", "changed", "nested"
)
MARKERS = {
    "non_changed": None,
    "removed": "- ",
    "added": "+ ",
    "changed": None
}
STOP_LIST = [ADDED, REMOVED, NON_CHANGED]


def pack_file(dictionary, extension):
    if extension == ".json":
        file = json.dumps(dictionary, indent=2)
        test_file = open("test.json", "w")
        test_file.write(file)
        test_file.close()
    else:
        file = yaml.dump(dictionary, default_flow_style=False)
        test_file = open("test.yaml", "w")
        test_file.write(file)
        test_file.close()
    print(file)


def make_result(key, value, spaces, marker=None):
    string_spaces = "" + (" " * spaces)
    if not marker:
        marker = "  "
    return f"{string_spaces}{marker} {key}: {value}\n"


def render_result(dictionary, spaces=2):
    result = "{" + "\n"
    for key, value in dictionary.items():
        if value[0] == NESTED:
            result += make_result(key, render_result(value[1], spaces=spaces+4), spaces)  # noqa: E501

        elif isinstance(value[1], dict) and not value[0] == CHANGED :  # noqa: E501
            result += make_result(key, render_result(value[1], spaces=spaces+4),
                                  spaces=spaces, marker=MARKERS[value[0]])  # noqa: E501

        elif value[0] == CHANGED:
            result += make_result(key, value[2], spaces=spaces, marker="- ")
            result += make_result(key, value[1], spaces=spaces, marker="+ ")
        else:
            result += make_result(key, value[1], spaces=spaces, marker=MARKERS[value[0]])  # noqa: E501

    result += ' ' * (spaces - 2) + '}' + "\n"
    return result


file1 = open_file("/home/tatoxa/python_projects/python-project-lvl2/tests/fixtures/test_files/before_2.json")
file2 = open_file("/home/tatoxa/python_projects/python-project-lvl2/tests/fixtures/test_files/after_2.json")
diff = generate_diff(file1, file2)
print(render_result(diff))
