from collections import OrderedDict


def mark_difference(key, before, after):
    difference = {}
    if key in after and before[key] != after[key]:
        difference[key] = mark_removed(key, before, after)
        difference[key] = mark_added(key, before, after)
    return difference


def mark_removed(key, dictionary_before, dictionary_after):
    if key not in dictionary_after:
        key = (REMOVED, dictionary_before[key])
    return key


def mark_added(key, dictionary_before, dictionary_after):
    if key not in dictionary_before:
        key = (ADDED, dictionary_after[key])
    return key


def mark_non_changed(key, dictionary_before, dictionary_after):
    if key in dictionary_after and dictionary_before[key] == dictionary_after[key]:
        key = (NON_CHANGED, dictionary_before[key])
    return key


REMOVED, ADDED, NON_CHANGED, CHANGED = "removed", "added", "non_changed", "changed"


def generate_diff(before, after):
    for key, value in before.items():
        if key not in after:
            before[key] = (REMOVED, value)

        elif isinstance(value, (dict, list)):
            if key not in after:
                before[key] = (REMOVED, value)
                continue

            before[key] = (NON_CHANGED, value)
            generate_diff(value, after[key])

        elif key not in after:
            before[key] = (REMOVED, before[key])
        elif key in after and value != after[key]:
            before[key] = (CHANGED, value, after[key])
        else:
            before[key] = (NON_CHANGED, value)

    for key, value in after.items():
        if isinstance(value, (dict, list)):
            if key not in before:
                before[key] = (ADDED, value)
                continue
        before[key] = (ADDED, value)

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



