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
        if isinstance(before[key], dict):
            result[key] = (REMOVED, generate_diff(before[key], before[key]))
        else:
            result[key] = (REMOVED, before[key])

    for key in after.keys() - before.keys():
        if isinstance(after[key], dict):
            result[key] = (ADDED, generate_diff(after[key], after[key]))
        else:
            result[key] = (ADDED, after[key])
    return result
