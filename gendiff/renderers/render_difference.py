REMOVED, ADDED, NON_CHANGED, CHANGED, NESTED = (
    "removed", "added", "non_changed", "changed", "nested"
)
MARKERS = {
    "non_changed": None,
    "removed": "- ",
    "added": "+ ",
    "changed": None
}


def make_result(key, value, spaces, marker=None):
    string_spaces = "" + (" " * spaces)
    if not marker:
        marker = "  "
    return f"{string_spaces}{marker} {key}: {value}\n"


def render_result(dictionary, spaces=2):
    result = "{" + "\n"
    for key, value in dictionary.items():
        if value[0] == NESTED:
            result += make_result(key, render_result(value[1], spaces=spaces+4), spaces)  # noqa: E501

        elif isinstance(value[1], dict) and not value[0] == CHANGED:  # noqa: E501
            result += make_result(key, render_result(value[1], spaces=spaces+4),    # noqa: E501
                                  spaces=spaces, marker=MARKERS[value[0]])

        elif value[0] == CHANGED:
            result += make_result(key, value[2], spaces=spaces, marker="- ")
            result += make_result(key, value[1], spaces=spaces, marker="+ ")
        else:
            result += make_result(key, value[1], spaces=spaces, marker=MARKERS[value[0]])  # noqa: E501

    result += ' ' * (spaces - 2) + '}' + "\n"
    return result
