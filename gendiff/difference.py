from gendiff.files import read_file

REMOVED, ADDED, NON_CHANGED, CHANGED, NESTED = (
    "removed", "added", "non_changed", "changed", "nested"
)


def mark_keys(dictionary1, dictionary2):
    result = {
        NON_CHANGED: dictionary1.keys() & dictionary2.keys(),
        REMOVED: dictionary1.keys() - dictionary2.keys(),
        ADDED: dictionary2.keys() - dictionary1.keys()}
    return result


def generate_diff(before, after):
    key_status = mark_keys(before, after)
    result = {}
    for key in key_status[NON_CHANGED]:
        if before[key] == after[key]:
            result[key] = (NON_CHANGED, before[key])
        else:
            if isinstance(before[key], dict) and isinstance(after[key], dict):
                result[key] = (NESTED, generate_diff(before[key], after[key]))
            else:
                result[key] = (CHANGED, (before[key], after[key]))

    for key in key_status[REMOVED]:
        result[key] = (REMOVED, before[key])

    for key in key_status[ADDED]:
        result[key] = (ADDED, after[key])

    return result


file1 = read_file("/home/tatoxa/python_projects/python-project-lvl2/tests/fixtures/test_before_2.json")
file2 = read_file("/home/tatoxa/python_projects/python-project-lvl2/tests/fixtures/test_after_2.json")
# print(generate_diff(file1, file2))
