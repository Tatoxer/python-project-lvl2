from gendiff.open_file import open_file


REMOVED, ADDED, NON_CHANGED, CHANGED, NESTED = (
    "removed", "added", "non_changed", "changed", "nested"
)


def mark_removed_key(key, value, dictionary_before, dictionary_after):
    if key not in dictionary_after:
        dictionary_before[key] = (REMOVED, value)


def mark_changed_key(key, dictionary_before, dictionary_after):
    if key in dictionary_after and dictionary_before[key] != dictionary_after[key]:  # noqa: E501
        dictionary_before[key] = (CHANGED, dictionary_before[key], dictionary_after[key])  # noqa: E501


def mark_non_changed_key(key, dictionary_before, dictionary_after):
    if key in dictionary_after and dictionary_before[key] == dictionary_after[key]:  # noqa: E501
        dictionary_before[key] = (NON_CHANGED, dictionary_before[key])


def mark_added_key(dictionary_before, dictionary_after):
    if isinstance(dictionary_after, dict):
        for key, value in dictionary_after.items():
            if isinstance(value, dict) and key not in dictionary_before:
                dictionary_before[key] = (ADDED, value)

                if isinstance(value, dict):
                    generate_diff(value, value)

            elif key not in dictionary_before:
                dictionary_before[key] = (ADDED, value)


def generate_diff(before, after):
    for key, value in before.items():
        if isinstance(value, dict):
            if key not in after:
                before[key] = (REMOVED, value)
                if isinstance(value, dict):
                    generate_diff(value, value)

            else:
                before[key] = (NESTED, value)
                generate_diff(value, after[key])

        else:
            mark_removed_key(key, value, before, after)
            mark_changed_key(key, before, after)
            mark_non_changed_key(key, before, after)

    mark_added_key(before, after)
    return before


file_1 = open_file("/home/tatoxa/python_projects/python-project-lvl2/tests/fixtures/test_files/empty.json")
file_2 = open_file("/home/tatoxa/python_projects/python-project-lvl2/tests/fixtures/test_files/before_2.json")



if __name__ == "__main__":
    print(generate_diff(file_1, file_2))