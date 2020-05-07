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


def generate_diff(file_1, file_2):
    difference = {}
    for key, value in file_1.items():
        if key in file_2:
            if value != file_2[key]:
                formatted_key = f'- {key}'
                difference[formatted_key] = file_1[key]

                formatted_key = f'+ {key}'
                difference[formatted_key] = file_2[key]

        if key not in file_2:
            formatted_key = f'- {key}'
            difference[formatted_key] = file_1[key]

    for key, value in file_2.items():
        if key not in file_1:
            formatted_key = f'+ {key}'
            difference[formatted_key] = file_2[key]

    for key, value in difference.items():
        print(key + ":" + str(value))


print(generate_diff(before, after))