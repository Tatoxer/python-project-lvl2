from gendiff.files import read_file
REMOVED, ADDED, NON_CHANGED, CHANGED, NESTED = (
    "removed", "added", "non_changed", "changed", "nested"
)


def generate_diff(before, after):
    result = {}
    for key in before.keys() & after.keys():
        if before[key] == after[key]:
            result[key] = (NON_CHANGED, before[key])
        else:
            if isinstance(before[key], dict) and isinstance(after[key], dict):
                result[key] = (NESTED, generate_diff(before[key], after[key]))
            else:
                result[key] = (CHANGED, (before[key], after[key]))

    for key in before.keys() - after.keys():
        result[key] = (REMOVED, before[key])

    for key in after.keys() - before.keys():
        result[key] = (ADDED, after[key])

    return result


file1 = read_file("/home/tatoxa/python_projects/python-project-lvl2/tests/fixtures/test_before_2.json")
file2 = read_file('/home/tatoxa/python_projects/python-project-lvl2/tests/fixtures/test_after_2.json')
print(generate_diff(file1, file2))
