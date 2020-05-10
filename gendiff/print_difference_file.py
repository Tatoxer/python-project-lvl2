import json
import yaml


def convert_dictionary_to_string(dictionary):
    string = ""
    for key, value in dictionary.items():
        string += f'\n{key}: {str(value)}\n'
    return string


def print_keys_values(dictionary):
    for key, value in dictionary.items():
        print(f'{key}: {value}')


def pack_and_print_file(dictionary, extension):
    print('extension = ' + str(extension))
    string = convert_dictionary_to_string(dictionary)
    if extension == ".json":
        file = json.dumps(dictionary, indent=2)
        test_file = open("test.json", "w")
        test_file.write(file)
        test_file.close()
    else:
        file = yaml.dump(string, default_flow_style=False)
        test_file = open("test.yaml", "w")
        test_file.write(file)
        test_file.close()
    print(file)
