#!/usr/bin/env python3
from gendiff import generate_diff, render_dictionary, \
    render_plain, render_json
from gendiff.files import read_file
import argparse

RENDERERS = {
    "plain": render_plain,
    "dictionary": render_dictionary,
    "json": render_json
}

parser = argparse.ArgumentParser(description="Generate difference")
parser.add_argument("file1", type=str,  help='path/to/file1')
parser.add_argument("file2", type=str,  help='path/to/file2')
parser.add_argument('-f', '--format', choices=RENDERERS.keys(), default="plain",    # noqa: E501
                    help='set printing result format'
                         'available: "plain", "dictionary", "json". '
                         'Default: plain')

args = parser.parse_args()


def main():
    path1 = args.file1
    path2 = args.file2
    file_1 = read_file(path1)
    file_2 = read_file(path2)
    difference = generate_diff(file_1, file_2)
    renderer = RENDERERS[args.format]
    print(renderer(difference))


if __name__ == "__main__":
    main()
