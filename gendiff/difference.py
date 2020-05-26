from gendiff.files import read_file

REMOVED, ADDED, NON_CHANGED, CHANGED, NESTED = (
    "removed", "added", "non_changed", "changed", "nested"
)


def mark_keys(dictionary1, dictionary2):
    result = {
        NON_CHANGED: (dictionary1.keys() & dictionary2.keys()),
        REMOVED: dictionary1.keys() - dictionary2.keys(),
        ADDED: dictionary2.keys() - dictionary1.keys()}
    return result


def generate_diff(before, after):
    key_status = mark_keys(before, after)
    for key, value in before.items():
        if isinstance(value, dict) and key in key_status[NON_CHANGED]:
            before[key] = (NESTED, value)
            generate_diff(value, after[key])

        elif key in key_status[REMOVED]:
            if isinstance(value, dict):
                before[key] = (REMOVED, value)
                generate_diff(value, value)
            else:
                before[key] = (REMOVED, value)

        elif key in after and not value == after[key]:
            before[key] = (CHANGED, (value, after[key]))

        else:
            before[key] = (NON_CHANGED, value)

    for key, value in after.items():
        if key in key_status[ADDED]:
            if isinstance(after[key], dict):
                before[key] = (ADDED, value)
                generate_diff(value, value)
            else:
                before[key] = (ADDED, value)

    return before


file1 = read_file("/home/tatoxa/python_projects/python-project-lvl2/tests/fixtures/test_before_2.json")
file2 = read_file("/home/tatoxa/python_projects/python-project-lvl2/tests/fixtures/test_after_2.json")
#print(generate_diff(file1, file2))
