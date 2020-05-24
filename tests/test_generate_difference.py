from gendiff import generate_diff, render_dictionary, open_file, \
    render_plain, render_json


"""Test files"""
EMPTY_FILE = "tests/fixtures/test_empty.json"
ADD_ONE = "tests/fixtures/test_add_one.json"
BEFORE = "tests/fixtures/test_before.json"
AFTER = "tests/fixtures/test_after.json"
BEFORE_2 = "tests/fixtures/test_before_2.json"
AFTER_2 = "tests/fixtures/test_after_2.json"
BEFORE_3 = "tests/fixtures/test_before_3.json"

"""Answer files"""
PLUS_ONE = "tests/fixtures/answer_plus_one.txt"
MINUS_ONE = "tests/fixtures/answer_minus_one.txt"
REMOVED_AND_ADDED = "tests/fixtures/answer_removed_and_added.txt"
REMOVED_ALL = "tests/fixtures/answer_removed_all.txt"
ADDED_ALL = "tests/fixtures/answer_added_all.txt"
CHANGES = "tests/fixtures/answer_changes.txt"
PLAIN_CHANGES = "tests/fixtures/answer_plain_changes.txt"
PLAIN_REMOVE_ALL = "tests/fixtures/answer_plain_remove_all.txt"
PLAIN_ADD_ALL = "tests/fixtures/answer_plain_add_all.txt"
PLAIN_ADD_COMPLEX = "tests/fixtures/answer_plain_add_complex_values.txt"
PLAIN_REMOVE_COMPLEX = "tests/fixtures/answer_plain_remove_complex_values.txt"
JSON_CHANGES = "tests/fixtures/answer_json_changes.txt"


def read_txt(path_to_file):
    with open(path_to_file, "r") as answer:
        expected = answer.read()
    return expected


def test_empty():
    file_1 = open_file(EMPTY_FILE)
    assert generate_diff(file_1, file_1) == {}


def test_add_one_to_empty():
    file_1 = open_file(EMPTY_FILE)
    file_2 = open_file(ADD_ONE)
    expected = read_txt(PLUS_ONE)
    difference = generate_diff(file_1, file_2)
    assert render_dictionary(difference) == expected


def test_remove_one_to_empty():
    file_1 = open_file(ADD_ONE)
    file_2 = open_file(EMPTY_FILE)
    expected = read_txt(MINUS_ONE)
    difference = generate_diff(file_1, file_2)
    assert render_dictionary(difference) == expected


def test_removed_and_added():
    file_1 = open_file(BEFORE)
    file_2 = open_file(AFTER)
    expected = read_txt(REMOVED_AND_ADDED)
    difference = generate_diff(file_1, file_2)
    assert render_dictionary(difference) == expected


def test_remove_all():
    file_1 = open_file(BEFORE_2)
    file_2 = open_file(EMPTY_FILE)
    expected = read_txt(REMOVED_ALL)
    difference = generate_diff(file_1, file_2)
    assert render_dictionary(difference) == expected


def test_add_all():
    file_1 = open_file(EMPTY_FILE)
    file_2 = open_file(BEFORE_2)
    expected = read_txt(ADDED_ALL)
    difference = generate_diff(file_1, file_2)
    assert render_dictionary(difference) == expected


def test_changes():
    file_1 = open_file(BEFORE_2)
    file_2 = open_file(AFTER_2)
    expected = read_txt(CHANGES)
    difference = generate_diff(file_1, file_2)
    assert render_dictionary(difference) == expected


def test_plain_changes():
    file_1 = open_file(BEFORE_2)
    file_2 = open_file(AFTER_2)
    expected = read_txt(PLAIN_CHANGES)
    difference = generate_diff(file_1, file_2)
    assert render_plain(difference) == expected


def test_plain_remove_all():
    file_1 = open_file(BEFORE_2)
    file_2 = open_file(EMPTY_FILE)
    expected = read_txt(PLAIN_REMOVE_ALL)
    difference = generate_diff(file_1, file_2)
    assert render_plain(difference) == expected


def test_plain_add_all():
    file_1 = open_file(EMPTY_FILE)
    file_2 = open_file(BEFORE_2)
    expected = read_txt(PLAIN_ADD_ALL)
    difference = generate_diff(file_1, file_2)
    assert render_plain(difference) == expected


def test_plain_add_complex_value():
    file_1 = open_file(BEFORE_2)
    file_2 = open_file(BEFORE_3)
    expected = read_txt(PLAIN_ADD_COMPLEX)
    difference = generate_diff(file_1, file_2)
    assert render_plain(difference) == expected


def test_plain_remove_complex_value():
    file_1 = open_file(BEFORE_3)
    file_2 = open_file(BEFORE_2)
    expected = read_txt(PLAIN_REMOVE_COMPLEX)
    difference = generate_diff(file_1, file_2)
    assert render_plain(difference) == expected


def test_json_difference():
    file_1 = open_file(BEFORE_2)
    file_2 = open_file(AFTER_2)
    expected = read_txt(JSON_CHANGES)
    difference = generate_diff(file_1, file_2)
    assert render_json(difference) == expected
