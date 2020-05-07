import argparse


parser = argparse.ArgumentParser(description="Generate difference")
parser.add_argument("file_1", type=str, help='path to file_1')
parser.add_argument("file_2", type=str, help='path to file_2')
parser.add_argument('-f', '--FORMAT', type=str, help='set format for output file')
args = parser.parse_args()
print(args)


def main():
    print("Hello")
