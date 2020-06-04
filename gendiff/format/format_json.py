import json


def format_json(dictionary, no_colors=False):
    return json.dumps(dictionary, indent=2, sort_keys=True)
