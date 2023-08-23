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
