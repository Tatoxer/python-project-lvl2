from gendiff.generate_difference import generate_diff
from gendiff.renderers.render_difference import render_result
from gendiff.open_file import open_file
from gendiff.renderers.plain_render import render_plain


test_files = {
    "empty_file": "tests/fixtures/test_files/empty.json",
    "add_one": "tests/fixtures/test_files/add_one.json",
    "before": "tests/fixtures/test_files/before.json",
    "after": "tests/fixtures/test_files/after.json",
    "before_2": "tests/fixtures/test_files/before_2.json",
    "after_2": "tests/fixtures/test_files/after_2.json",
    "before_3": "tests/fixtures/test_files/before_3.json",
}
answer_files = {
    "right_plus_one": "tests/fixtures/right_answers/plus_one.txt",
    "right_minus_one": "tests/fixtures/right_answers/minus_one.txt",
    "right_removed_and_added": "tests/fixtures/right_answers/removed_and_added.txt",
    "right_removed_all": "tests/fixtures/right_answers/removed_all.txt",
    "right_added_all": "tests/fixtures/right_answers/added_all.txt",
    "right_changes": "tests/fixtures/right_answers/changes.txt",
    "plain_changes": "tests/fixtures/right_answers/plain_changes.txt",
    "plain_remove_all": "tests/fixtures/right_answers/plain_remove_all.txt",
    "plain_add_all": "tests/fixtures/right_answers/plain_add_all.txt",
    "plain_add_complex": "tests/fixtures/right_answers/plain_add_complex_values.txt",
    "plain_remove_complex": "tests/fixtures/right_answers/plain_remove_complex_values.txt"
}


def open_txt(dir_):
    with open(dir_, "r") as answer:
        expected = answer.read()
    return expected


def test_empty():
    file_1 = open_file(test_files["empty_file"])
    assert generate_diff(file_1, file_1) == {}


def test_add_one_to_empty():
    file_1 = open_file(test_files["empty_file"])
    file_2 = open_file(test_files["add_one"])
    expected = open_txt(answer_files["right_plus_one"])
    difference = generate_diff(file_1, file_2)
    assert render_result(difference) == expected


def test_remove_one_to_empty():
    file_1 = open_file(test_files["add_one"])
    file_2 = open_file(test_files["empty_file"])
    expected = open_txt(answer_files["right_minus_one"])
    difference = generate_diff(file_1, file_2)
    assert render_result(difference) == expected


def test_removed_and_added():
    file_1 = open_file(test_files["before"])
    file_2 = open_file(test_files["after"])
    expected = open_txt(answer_files["right_removed_and_added"])
    difference = generate_diff(file_1, file_2)
    assert render_result(difference) == expected


def test_remove_all():
    file_1 = open_file(test_files["before_2"])
    file_2 = open_file(test_files["empty_file"])
    expected = open_txt(answer_files["right_removed_all"])
    difference = generate_diff(file_1, file_2)
    assert render_result(difference) == expected


def test_add_all():
    file_1 = open_file(test_files["empty_file"])
    file_2 = open_file(test_files["before_2"])
    expected = open_txt(answer_files["right_added_all"])
    difference = generate_diff(file_1, file_2)
    assert render_result(difference) == expected


def test_changes():
    file_1 = open_file(test_files["before_2"])
    file_2 = open_file(test_files["after_2"])
    expected = open_txt(answer_files["right_changes"])
    difference = generate_diff(file_1, file_2)
    assert render_result(difference) == expected


def test_plain_changes():
    file_1 = open_file(test_files["before_2"])
    file_2 = open_file(test_files["after_2"])
    expected = open_txt(answer_files["plain_changes"])
    difference = generate_diff(file_1, file_2)
    assert render_plain(difference) == expected


def test_plain_remove_all():
    file_1 = open_file(test_files["before_2"])
    file_2 = open_file(test_files["empty_file"])
    expected = open_txt(answer_files["plain_remove_all"])
    difference = generate_diff(file_1, file_2)
    assert render_plain(difference) == expected


def test_plain_add_all():
    file_1 = open_file(test_files["empty_file"])
    file_2 = open_file(test_files["before_2"])
    expected = open_txt(answer_files["plain_add_all"])
    difference = generate_diff(file_1, file_2)
    assert render_plain(difference) == expected


def test_plain_add_complex_value():
    file_1 = open_file(test_files["before_2"])
    file_2 = open_file(test_files["before_3"])
    expected = open_txt(answer_files["plain_add_complex"])
    difference = generate_diff(file_1, file_2)
    assert render_plain(difference) == expected


def test_plain_remove_complex_value():
    file_1 = open_file(test_files["before_3"])
    file_2 = open_file(test_files["before_2"])
    expected = open_txt(answer_files["plain_remove_complex"])
    difference = generate_diff(file_1, file_2)
    assert render_plain(difference) == expected
