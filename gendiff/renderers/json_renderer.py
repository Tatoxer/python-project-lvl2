import json


def render_json(dictionary):
    return json.dumps(dictionary, indent=2)
