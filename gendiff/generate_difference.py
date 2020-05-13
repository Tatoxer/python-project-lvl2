REMOVED, ADDED, NON_CHANGED, CHANGED, NESTED = "removed", "added", "non_changed", "changed", "nested"


def generate_diff(before, after):
    for key, value in before.items():
        if isinstance(value, dict):
            if key not in after:
                before[key] = (REMOVED, value)
                continue

            before[key] = (NESTED, value)
            generate_diff(value, after[key])

        else:
            if key not in after:
                before[key] = (REMOVED, value)

            if key in after and before[key] != after[key]:
                before[key] = (CHANGED, before[key], after[key])

            elif key in after and before[key] == after[key]:
                before[key] = (NON_CHANGED, before[key])

    for key, value in after.items():
        if isinstance(value, dict) and key not in before:
            before[key] = (ADDED, value)
            continue

    return before
