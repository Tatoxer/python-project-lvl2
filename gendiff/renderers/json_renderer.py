import json


def render_json(string):
    result = json.dumps(string, sort_keys=True, indent=2)
    return result
