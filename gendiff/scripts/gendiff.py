#!/usr/bin/env python3
from gendiff import generate_difference, generate_cli_settings, open_file, print_difference_file


def main():
    dir_1, dir_2, extension = generate_cli_settings.generate_description_settings()
    file_1 = open_file.open_file(dir_1)
    file_2 = open_file.open_file(dir_2)
    difference = generate_difference.generate_diff(file_1, file_2)
    print_difference_file.render_result(difference)


if __name__ == "__main__":
    main()
