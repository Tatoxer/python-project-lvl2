from gendiff.open_file import open_file


KEYS_STATUS = (UNMODIFIED, DELETED, ADDED, REPLACED, NESTED) = (
    'unmodified', 'deleted', 'added', 'replaced', 'nested'
)


def build_tree(data):
    result = {}
    for key in data:
        if isinstance(data[key], dict):
            result[key] = (NESTED, build_tree(data[key]))
        else:
            result[key] = (UNMODIFIED, data[key])
    return result


def ternary_safe_put(status, value, second_value):
    result = None
    if isinstance(value, dict) and not isinstance(second_value, dict):
        result = status, build_tree(value), second_value
    elif not isinstance(value, dict) and isinstance(second_value, dict):
        result = status, value, build_tree(second_value)
    else:
        result = status, value, second_value
    return result


def safe_put(status, value):
    result = None
    if isinstance(value, dict):
        result = status, build_tree(value)
    else:
        result = status, value
    return result


def build_status(first_dict, second_dict):
    result = {}
    result[UNMODIFIED] = first_dict.keys() & second_dict.keys()
    result[DELETED] = first_dict.keys() - second_dict.keys()
    result[ADDED] = second_dict.keys() - first_dict.keys()
    return result


def build_diff(primary_data, modified_data):
    diff = {}
    keys_status = build_status(primary_data, modified_data)
    for key, value in primary_data.items():
        if key in keys_status[UNMODIFIED]:
            common_key = modified_data[key]
            if isinstance(value, dict) and isinstance(common_key,
                                                      dict):
                diff[key] = (NESTED, build_diff(value,
                             common_key))
            elif value == common_key:
                diff[key] = (UNMODIFIED, value)
            else:
                diff[key] = ternary_safe_put(REPLACED, common_key,
                                             value)
        elif key in keys_status[DELETED]:
            diff[key] = safe_put(DELETED, value)
    for key, value in modified_data.items():
        if key in keys_status[ADDED]:
            diff[key] = safe_put(ADDED, value)
    return diff


file_1 = open_file("/home/tatoxa/python_projects/python-project-lvl2/tests/fixtures/test_files/before_2.json")
file_2 = open_file("/home/tatoxa/python_projects/python-project-lvl2/tests/fixtures/test_files/after_2.json")
print(build_diff(file_1, file_2))