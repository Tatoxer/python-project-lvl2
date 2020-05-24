import os.path
import json
import yaml


SUPPORTED_FORMATS = ["json", "yaml", "yml"]
YAML_FORMATS = ["yaml", "yml"]


def read_file(dir_1):
    dir_1 = os.path.abspath(dir_1)
    file_format = os.path.splitext(dir_1)
    file_format = file_format[1].lower()

    if file_format == ".json":
        result = json.load(open(dir_1))

    elif file_format in YAML_FORMATS:
        result = yaml.safe_load(open(dir_1))

    else:
        result = ValueError
    return result

