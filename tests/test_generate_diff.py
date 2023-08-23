from gendiff.generate_diff import generate_diff
import pytest


json1 = "tests/fixtures/file1.json"
json2 = "tests/fixtures/file2.json"
yaml1 = "tests/fixtures/file1.yaml"
yaml2 = "tests/fixtures/file2.yaml"
json1_tree = "tests/fixtures/file1_tree.json"
json2_tree = "tests/fixtures/file2_tree.json"
yaml1_tree = "tests/fixtures/file1_tree.yaml"
yaml2_tree = "tests/fixtures/file2_tree.yaml"
result_stylish_flat = "tests/fixtures/correct_result.txt"
result_stylish = "tests/fixtures/correct_result_tree.txt"
result_plain = "tests/fixtures/correct_result_tree_plain.txt"
result_json = "tests/fixtures/correct_result_tree_json.txt"
result_json_flat = "tests/fixtures/correct_result_json_format.txt"

format_name = ['stylish', 'plain', 'json']


@pytest.mark.parametrize(
    'file_path1, file_path2, format_name, expected',
    [
        (json1, json2, format_name[0], result_stylish_flat),
        (yaml1, yaml2, format_name[0], result_stylish_flat),
        (json1_tree, json2_tree, format_name[0], result_stylish),
        (yaml1_tree, yaml2_tree, format_name[0], result_stylish),
        (json1_tree, json2_tree, format_name[1], result_plain),
        (yaml1_tree, yaml2_tree, format_name[1], result_plain),
        (json1, json2, format_name[2], result_json_flat),
        (yaml1, yaml2, format_name[2], result_json_flat),
        (json1_tree, json2_tree, format_name[2], result_json),
        (yaml1_tree, yaml2_tree, format_name[2], result_json)
    ]
)
def test_generate_diff(file_path1, file_path2, format_name, expected):
    exp = open(expected).read().strip()
    assert generate_diff(file_path1, file_path2, format_name) == exp
#def test_generate_diff():
#    diff_json = generate_diff(
#        "tests/fixtures/file1.json", "tests/fixtures/file2.json"
#    )
#    assert diff_json == open("tests/fixtures/correct_result.txt").read()
#
#    diff_json2 = generate_diff(
#        "tests/fixtures/file1_tree.json", "tests/fixtures/file2_tree.json"
#    )
#    assert diff_json2 == open("tests/fixtures/correct_result_tree.txt").read()
#
#    diff_yaml = generate_diff(
#        "tests/fixtures/file1.yaml", "tests/fixtures/file2.yaml"
#    )
#    assert diff_yaml == open("tests/fixtures/correct_result.txt").read()
#
#    diff_yaml2 = generate_diff(
#        "tests/fixtures/file1_tree.yaml", "tests/fixtures/file2_tree.yaml"
#    )
#    assert diff_yaml2 == open("tests/fixtures/correct_result_tree.txt").read()
#
#    diff_json2_plain = generate_diff(
#        "tests/fixtures/file1_tree.json", "tests/fixtures/file2_tree.json",
#        format_name='plain'
#    )
#    assert diff_json2_plain == open(
#        "tests/fixtures/correct_result_tree_plain.txt"
#    ).read().strip()
#
#    diff_yaml2_plain = generate_diff(
#        "tests/fixtures/file1_tree.yaml", "tests/fixtures/file2_tree.yaml",
#        format_name='plain'
#    )
#    assert diff_yaml2_plain == open(
#        "tests/fixtures/correct_result_tree_plain.txt"
#    ).read().strip()
#
#    diff_json3_json = generate_diff(
#        "tests/fixtures/file1_tree.json", "tests/fixtures/file2_tree.json",
#        format_name='json'
#    )
#    assert diff_json3_json == open(
#        "tests/fixtures/correct_result_tree_json.txt"
#    ).read().strip()
#
#    diff_yaml3_json = generate_diff(
#        "tests/fixtures/file1_tree.yaml", "tests/fixtures/file2_tree.yaml",
#        format_name='json'
#    )
#    assert diff_yaml3_json == open(
#        "tests/fixtures/correct_result_tree_json.txt"
#    ).read().strip()
#
#    diff_json_to_json = generate_diff(
#        "tests/fixtures/file1.json", "tests/fixtures/file2.json",
#        format_name='json'
#    )
#    assert diff_json_to_json == open(
#        "tests/fixtures/correct_result_json_format.txt"
#    ).read().strip()
