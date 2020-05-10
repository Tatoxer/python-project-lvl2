import argparse


def generate_description_settings():
    parser = argparse.ArgumentParser(description="Generate difference")
    parser.add_argument("file_1", type=str, help='path/to/file_1')
    parser.add_argument("file_2", type=str, help='path/to/file_2')
    parser.add_argument('-f', '--FORMAT', type=str, default=".json",
                        help='set format for output file')
    args = parser.parse_args()
    # print(args)
    return args.file_1, args.file_2
