import argparse

before = {
  "host": "hexlet.io",
  "timeout": 50,
  "proxy": "123.234.53.22"
}

after = {
  "timeout": 20,
  "verbose": "true",
  "host": "hexlet.io"
}


def make_description():
    parser = argparse.ArgumentParser(description="Generate difference")
    parser.add_argument("file_1", type=str, help='path to file_1')
    parser.add_argument("file_2", type=str, help='path to file_2')
    parser.add_argument('-f', '--FORMAT', type=str, default=".json", help='set format for output file')
    args = parser.parse_args()
    print(args)
    return args.file_1, args.file_2


def generate_added_key(key, value):
    formatted_key = f'+ {key}'
    return {formatted_key: value}


def generate_removed_key(key, value):
    formatted_key = f'- {key}'
    return {formatted_key: value}


def generate_diff(file_1, file_2):
    difference = {}
    for key, value in file_1.items():
        if key in file_2 and value != file_2[key]:
            difference.update(generate_removed_key(key, value))
            difference.update(generate_added_key(key, file_2[key]))

        if key not in file_2:
            difference.update(generate_removed_key(key, file_1[key]))

    for key, value in file_2.items():
        if key not in file_1:
            difference.update(generate_added_key(key, file_2[key]))

    for key, value in difference.items():
        print(f'{key}: {str(value)}')


print(generate_diff(before, after))