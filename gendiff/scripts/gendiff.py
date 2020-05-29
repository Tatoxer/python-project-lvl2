#!/usr/bin/env python3
from gendiff import generate_diff, render_dictionary, \
    render_plain, render_json
from gendiff import files
import argparse


RENDERERS = {
    "plain": render_plain,
    "dictionary": render_dictionary,
    "json": render_json
}

parser = argparse.ArgumentParser(description="Generate difference")
parser.add_argument("file1", type=str,  help='path/to/file1')
parser.add_argument("file2", type=str,  help='path/to/file2')
parser.add_argument('-n', '--no_colors', action='store_true',
                    help='Print non colored result')
parser.add_argument('-f', '--format', choices=RENDERERS.keys(), default="plain",    # noqa: E501
                    help='set printing format result'
                         'available: "plain", "dictionary", "json". '
                         'Default: plain')

args = parser.parse_args()


def main():
    path1 = args.file1
    path2 = args.file2
    no_colors = args.no_colors
    try:
        file_1 = files.read_file(path1)
        file_2 = files.read_file(path2)
        difference = generate_diff(file_1, file_2)
        renderer = RENDERERS[args.format]
        print(renderer(difference, no_colors))
    except AttributeError:
        print("You entered unsupported file format")
        print("Supported formats are: \n'.json'\n'.yaml'\n'.yml'")


if __name__ == "__main__":
    main()
