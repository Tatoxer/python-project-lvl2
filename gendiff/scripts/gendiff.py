#!/usr/bin/env python3
from gendiff.generate_difference import generate_diff
from gendiff.generate_cli_settings import generate_description_settings
from gendiff.open_file import open_file
from gendiff.renderers.render_difference import render_result


def main():
    dir_1, dir_2, renderer = generate_description_settings()
    file_1 = open_file(dir_1)
    file_2 = open_file(dir_2)
    difference = generate_diff(file_1, file_2)
    print(render_result(difference))


if __name__ == "__main__":
    main()
