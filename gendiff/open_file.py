import os.path
import json
import yaml


SUPPORTED_FORMATS = ["json", "JSON", "yaml", "YAML", "yml", "YML"]
YAML_FORMATS = ["yaml", "YAML", "yml", "YML"]


def open_file(dir_1):
    dir_1 = os.path.abspath(dir_1)
    file_format = dir_1.split(".")
    if file_format[-1] == "json" or file_format[-1] == "JSON":
        file = json.load(open(dir_1))

    elif file_format[-1] in YAML_FORMATS:
        file = yaml.safe_load(open(dir_1))

    else:
        print(f"Sorry, format '{file_format[-1]}' is not supporting")
        print("Supported formats are:")
        print(", ".join(SUPPORTED_FORMATS))
        file = None
    return file
