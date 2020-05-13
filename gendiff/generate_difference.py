from collections import OrderedDict


def mark_changed_key(key, before, after):
    if key in after and before[key] != after[key]:
        key = (CHANGED, before[key], after[key])
    return key


def mark_removed_key(key, dictionary_before, dictionary_after):
    if key not in dictionary_after:
        key = (REMOVED, dictionary_before[key])
    return key


def mark_added_key(key, dictionary_before, dictionary_after):
    if key not in dictionary_before:
        key = (ADDED, dictionary_after[key])
    return key


def mark_non_changed_key(key, dictionary_before, dictionary_after):
    if key in dictionary_after and dictionary_before[key] == dictionary_after[key]:
        key = (NON_CHANGED, dictionary_before[key])
    return key


REMOVED, ADDED, NON_CHANGED, CHANGED = "removed", "added", "non_changed", "changed"


def generate_diff(before, after):
    for key, value in before.items():
        if isinstance(value, dict):
            if key not in after:
                before[key] = (REMOVED, value)
                continue

            before[key] = (NON_CHANGED, value)
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



