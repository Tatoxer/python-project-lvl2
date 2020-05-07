#!/usr/bin/env python3
import argparse
from gendiff import generate_difference


def print_description():
    parser = argparse.ArgumentParser(description="Generate difference")
    parser.add_argument("file_1", type=str, help='path to file_1')
    parser.add_argument("file_2", type=str, help='path to file_2')
    parser.add_argument('-f', '--FORMAT', type=str, default=".json", help='set format for output file')
    args = parser.parse_args()
    print(args)


def main():
    print_description()
    generate_difference.generate_diff()


if __name__ == "__main__":
    main()
