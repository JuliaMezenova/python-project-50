#!/usr/bin/env python3


from gendiff.generate_diff import generate_diff
from gendiff.parser import parse_data
from gendiff.cli import parse


def main():
    args = parse()
    print(
            generate_diff(args.first_file, args.second_file)
            )


if __name__ == '__main__':
    main()

