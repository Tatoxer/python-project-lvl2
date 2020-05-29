import os.path
import json
import yaml


YAML_FORMATS = ["yaml", "yml"]


def read_file(path):
    path = os.path.abspath(path)
    file_format = os.path.splitext(path)
    file_format = file_format[1].lower()
    result = ""
    if file_format == ".json":
        result = json.load(open(path))

    elif file_format in YAML_FORMATS:
        result = yaml.safe_load(open(path))

    return result
