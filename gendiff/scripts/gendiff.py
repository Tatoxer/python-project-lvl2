#!/usr/bin/env python3
from gendiff import generate_difference


def main():
    file_1, file_2 = generate_difference.make_description()
    generate_difference.generate_diff(file_1, file_2)


if __name__ == "__main__":
    main()
