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


file_1 = {
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
file_2 = {
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
dict_ = generate_diff(file_1, file_2)
dicti = {'common': ('nested', {'setting1': ('non_changed', 'Value 1'), 'setting2': ('removed', '200'), 'setting3': ('non_changed', "True"), 'setting6': ('removed', {'key': ('non_changed', 'value')}), 'setting4': ('added', 'blah blah'), 'setting5': ('added', {'key5': ('non_changed', 'value5')})}), 'group1': ('nested', {'baz': ('changed', 'bas', 'bars'), 'foo': ('non_changed', 'bar')}), 'group2': ('removed', {'abc': ('non_changed', '12345')}), 'group3': ('added', {'fee': ('non_changed', '100500')})}
print(render_plain(dict_))
