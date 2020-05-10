#!/usr/bin/env python3
from gendiff import generate_difference, generate_cli_settings, open_files


def main():
    dir_1, dir_2 = generate_cli_settings.generate_description_settings()
    file_1 = open_files.open_file(dir_1)
    file_2 = open_files.open_file(dir_2)
    generate_difference.generate_diff(file_1, file_2)


if __name__ == "__main__":
    main()
