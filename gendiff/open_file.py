import json
import os.path
import yaml


def open_file(dir_1):
    dir_1 = os.path.abspath(dir_1)
    file_format = dir_1[-4:]
    if file_format == ".json" or file_format == ".JSON":
        file = json.load(open(dir_1))
    else:
        file = yaml.safe_load(open(dir_1))
    return file

