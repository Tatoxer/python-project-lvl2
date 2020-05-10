from gendiff.generate_difference import generate_diff
from gendiff.open_files import open_file

empty_file = "gendiff/tests/fixtures/test_files/empty.json"
add_one = "gendiff/tests/fixtures/test_files/add_one.json"
before = "gendiff/tests/fixtures/test_files/before.json"
after = "gendiff/tests/fixtures/test_files/after.json"


def test_empty():
    file_1 = open_file(empty_file)
    assert generate_diff(file_1, file_1) == {}


def test_add_one_to_empty():
    file_1 = open_file(empty_file)
    file_2 = open_file(add_one)
    assert generate_diff(file_1, file_2) == {
        "+ add_one": "sample"
    }


def test_remove_one_to_empty():
    file_1 = open_file(empty_file)
    file_2 = open_file(add_one)
    assert generate_diff(file_2, file_1) == {
        "- add_one": "sample"
    }


def test_removed_and_added():
    file_1 = open_file(before)
    file_2 = open_file(after)
    assert generate_diff(file_1, file_2) == {
        "- timeout": "50",
        "+ timeout": "20",
        "- proxy": "123.234.53.22",
        "+ verbose": "True",
    }


def test_remove_all():
    file_1 = open_file(before)
    file_2 = open_file(empty_file)
    assert generate_diff(file_1, file_2) == {
        "- host": "hexlet.io",
        "- timeout": "50",
        "- proxy": "123.234.53.22"
    }


def test_add_all():
    file_1 = open_file(empty_file)
    file_2 = open_file(before)
    assert generate_diff(file_1, file_2) == {
        "+ host": "hexlet.io",
        "+ timeout": "50",
        "+ proxy": "123.234.53.22"
    }
