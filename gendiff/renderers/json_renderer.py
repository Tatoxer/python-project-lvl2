import json


def render_json(dictionary, no_colors=False):
    return json.dumps(dictionary, indent=2)
