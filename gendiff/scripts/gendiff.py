#!/usr/bin/env python3
from gendiff.generate_difference import generate_diff
from gendiff.generate_cli_settings import generate_description_settings
from gendiff.open_file import open_file
from gendiff.renderers.dictionary_render import render_dictionary, print_colored_dict
from gendiff.renderers.plain_render import render_plain, print_colored_plain


def choose_renderer(renderer, dictionary):
    if renderer == "dictionary":
        print_colored_dict(render_dictionary(dictionary))

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
