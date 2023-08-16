from gendiff.generate_diff import generate_diff


def test_generate_diff():
    diff_json = generate_diff("tests/fixtures/file1.json", "tests/fixtures/file2.json")
    assert diff_json == open("tests/fixtures/correct_result.txt").read()
    diff_json2 = generate_diff("tests/fixtures/file1_tree.json", "tests/fixtures/file2_tree.json")
    assert diff_json2 == open("tests/fixtures/correct_result_tree.txt").read()
    diff_yaml = generate_diff("tests/fixtures/file1.yaml", "tests/fixtures/file2.yaml")
    assert diff_yaml == open("tests/fixtures/correct_result.txt").read()
    diff_yaml2 = generate_diff("tests/fixtures/file1_tree.yaml", "tests/fixtures/file2_tree.yaml")
    assert diff_yaml2 == open("tests/fixtures/correct_result_tree.txt").read()
