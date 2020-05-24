#!/usr/bin/env python3
from gendiff import generate_diff, render_dictionary, \
    render_plain, render_json
from gendiff.files import read_file
import argparse


parser = argparse.ArgumentParser(description="Generate difference")
parser.add_argument("file1", type=str, help='path/to/file1')
parser.add_argument("file2", type=str, help='path/to/file2')
parser.add_argument('-f', '--format', type=str, default="plain",
                    help='set format for printing result '
                         'available: "plain", "dictionary", "json". '
                         'Default: plain')
args = parser.parse_args()


def check_renderer(renderer, dictionary):
    if renderer == "dictionary":
        print(render_dictionary(dictionary))

    elif renderer == "json":
        print(render_json(dictionary))

    else:
        print(render_plain(dictionary))


def main():
    path1 = args.file1
    path2 = args.file2
    renderer = args.format
    file_1 = read_file(path1)
    file_2 = read_file(path2)
    difference = generate_diff(file_1, file_2)
    check_renderer(renderer, difference)


if __name__ == "__main__":
    main()
