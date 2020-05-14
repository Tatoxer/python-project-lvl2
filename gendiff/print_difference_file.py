import json
import yaml
from gendiff.generate_difference import generate_diff


REMOVED, ADDED, NON_CHANGED, CHANGED, NESTED = "removed", "added", "non_changed", "changed", "nested"
MARKERS = {
    "non_changed": None,
    "removed": "- ",
    "added": "+ ",
    "changed": None
}


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


def add_added_result(key, value, result, spaces):
    if isinstance(value[1], dict) and value[0] == ADDED:
        result += make_result(key, value[1], spaces=spaces, marker=MARKERS[value[0]])
    return result


def render_result(dictionary, spaces=2):
    result = "{ " + "\n"
    for key, value in dictionary.items():
        if value[0] == NESTED:
            result += make_result(key, render_result(value[1], spaces=spaces+4), spaces)

        elif isinstance(value[1], dict) and value[0] == REMOVED:
            result += make_result(key, value[1], spaces=spaces, marker=MARKERS[value[0]])

        elif isinstance(value[1], dict) and value[0] == ADDED:
            result += make_result(key, value[1], spaces=spaces, marker=MARKERS[value[0]])

        elif isinstance(value[1], dict) and not value[0] == CHANGED:
            result += make_result(key, render_result(value[1], spaces=spaces), spaces=spaces, marker=MARKERS[value[0]])

        elif value[0] == CHANGED:
            if isinstance(value[1], dict) and not isinstance(value[2], dict):
                result += make_result(key, render_result(value[1], spaces=spaces+4), spaces=spaces, marker="+ ")
                result += make_result(key, value[2], spaces=spaces, marker="- ")

            elif not isinstance(value[1], dict) and isinstance(value[2], dict):
                result += make_result(key, value[1], spaces=spaces, marker="- ")
                result += make_result(key, render_result(key, value[2]), spaces=spaces, marker="+ ")

            else:
                result += make_result(key, value[2], spaces=spaces, marker="- ")
                result += make_result(key, value[1], spaces=spaces, marker="+ ")
        else:
            result += make_result(key, value[1], spaces=spaces, marker=MARKERS[value[0]])

    result += ' ' * (spaces-2) + '}'
    return result


test1 = {
  "common": {
    "setting1": "Value 1",
    "setting2": "200",
    "setting3": "true",
    "setting6": {
      "key": "value"
    }
  },
  "group1": {
    "baz": "bas",
    "foo": "bar"
  },
  "group2": {
    "abc": "12345"
  }
}
test2 = {
  "common": {
    "setting1": "Value 1",
    "setting3": "true",
    "setting4": "blah blah",
    "setting5": {
      "key5": "value5"
    }
  },

  "group1": {
    "foo": "bar",
    "baz": "bars"
  },

  "group3": {
    "fee": "100500"
  }
}

test_d = generate_diff(test1, test2)

print(render_result(test_d))
