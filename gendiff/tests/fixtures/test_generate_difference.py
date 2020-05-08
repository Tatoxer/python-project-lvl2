from gendiff.generate_difference import generate_diff

empty_file = "gendiff/tests/fixtures/test_files/empty.json"
add_one = "gendiff/tests/fixtures/test_files/add_one.json"
before = "gendiff/tests/fixtures/test_files/before.json"
after = "gendiff/tests/fixtures/test_files/after.json"


def test_empty():
    assert generate_diff(empty_file, empty_file) == {}


def test_add_one_to_empty():
    assert generate_diff(empty_file, add_one) == {
        "+ add_one": "sample"
    }


def test_remove_one_to_empty():
    assert generate_diff(add_one, empty_file) == {
        "- add_one": "sample"
    }


def test_removed_and_added():
    assert generate_diff(before, after) == {
        "- timeout": "50",
        "+ timeout": "20",
        "- proxy": "123.234.53.22",
        "+ verbose": "True",
    }


def test_remove_all():
    assert generate_diff(before, empty_file) == {
        "- host": "hexlet.io",
        "- timeout": "50",
        "- proxy": "123.234.53.22"
    }


def test_add_all():
    assert generate_diff(empty_file, before) == {
        "+ host": "hexlet.io",
        "+ timeout": "50",
        "+ proxy": "123.234.53.22"
    }
