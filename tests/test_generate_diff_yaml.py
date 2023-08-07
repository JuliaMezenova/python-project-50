from gendiff.generate_diff import generate_diff


def test_generate_diff():
    diff_yaml = generate_diff("tests/fixtures/file1.yaml", "tests/fixtures/file2.yaml")
    assert diff_yaml == open("tests/fixtures/correct_result.txt").read()
