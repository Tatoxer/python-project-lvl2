import argparse


parser = argparse.ArgumentParser(description="Generate difference")
parser.add_argument("file_1")
parser.add_argument("file_2")
args = parser.parse_args()
print(args)


def main():
    print("Hello")
