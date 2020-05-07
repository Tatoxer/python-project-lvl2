#!/usr/bin/env python3
from gendiff import generate_difference, generate_cli_settings


def main():
    dir_1, dir_2 = generate_cli_settings.generate_description_settings()
    generate_difference.generate_diff(dir_1, dir_2)


if __name__ == "__main__":
    main()
