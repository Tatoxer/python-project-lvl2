import json
import os.path
import yaml


def read_json(dir_1):
    file = json.load(open(dir_1))
    return file


def read_yaml(dir_1):
    file = yaml.safe_load(open(dir_1))
    return file


def open_file(dir_1):
    dir_1 = os.path.abspath(dir_1)
    file_1 = read_yaml(dir_1)
    return file_1
