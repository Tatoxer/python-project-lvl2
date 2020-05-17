#!/usr/bin/env python3
from gendiff import generate_diff, generate_description_settings, \
    open_file, render_dictionary, print_colored_dict, render_plain, \
    print_colored_plain, render_json


def choose_renderer(renderer, dictionary):
    if renderer == "dictionary":
        print_colored_dict(render_dictionary(dictionary))

    elif renderer == "json":
        print(render_json(dictionary))

    else:
        print_colored_plain(render_plain(dictionary))


def catch_errors(func):
    def safe_run():
        try:
            func()
        except Exception:
            print("")
    return safe_run


@catch_errors
def main():
    dir_1, dir_2, renderer = generate_description_settings()
    file_1 = open_file(dir_1)
    file_2 = open_file(dir_2)
    difference = generate_diff(file_1, file_2)
    choose_renderer(renderer, difference)


if __name__ == "__main__":
    main()
