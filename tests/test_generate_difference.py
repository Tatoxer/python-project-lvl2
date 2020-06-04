from gendiff import generate_diff, render_dictionary, \
    render_plain, render_json
from gendiff.files import read_file
import json

# Test files
EMPTY_FILE = "tests/fixtures/test_empty.json"
ADD_ONE = "tests/fixtures/test_add_one.json"
BEFORE = "tests/fixtures/test_before.json"
AFTER = "tests/fixtures/test_after.json"
BEFORE_2 = "tests/fixtures/test_before_2.json"
AFTER_2 = "tests/fixtures/test_after_2.json"
BEFORE_3 = "tests/fixtures/test_before_3.json"

# Answer files
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
JSON_CHANGES = "tests/fixtures/answer_json_changes.json"

TEST_DATA = [
    (EMPTY_FILE, ADD_ONE, PLUS_ONE, render_dictionary),
    (ADD_ONE, EMPTY_FILE, MINUS_ONE, render_dictionary),
    (BEFORE, AFTER, REMOVED_AND_ADDED, render_dictionary),
    (BEFORE_2, EMPTY_FILE, REMOVED_ALL, render_dictionary),
    (EMPTY_FILE, BEFORE_2, ADDED_ALL, render_dictionary),
    (BEFORE_2, AFTER_2, CHANGES, render_dictionary),
    (BEFORE_2, AFTER_2, PLAIN_CHANGES, render_plain),
    (BEFORE_2, EMPTY_FILE, PLAIN_REMOVE_ALL, render_plain),
    (EMPTY_FILE, BEFORE_2, PLAIN_ADD_ALL, render_plain),
    (BEFORE_2, BEFORE_3, PLAIN_ADD_COMPLEX, render_plain),
    (BEFORE_3, BEFORE_2, PLAIN_REMOVE_COMPLEX, render_plain),
]


def read_txt(path_to_file):
    with open(path_to_file, "r") as answer:
        expected = answer.read()
    return expected


def test_empty():
    assert generate_diff({}, {}) == {}


def test_values():
    for (before, after, answer, renderer) in TEST_DATA:
        file1 = read_file(before)
        file2 = read_file(after)
        expected = read_txt(answer)
        difference = generate_diff(file1, file2)
        assert renderer(difference, no_color=True) == expected


def test_json():
    file1 = read_file(BEFORE)
    file2 = read_file(AFTER)
    expected = json.load(open(JSON_CHANGES))
    expected = render_json(expected)
    difference = generate_diff(file1, file2)
    assert render_json(difference) == expected
