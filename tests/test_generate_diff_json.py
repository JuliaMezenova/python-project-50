from gendiff.generate_diff import generate_diff


def test_generate_diff():
    diff_json = generate_diff("tests/fixtures/file1.json", "tests/fixtures/file2.json")
    assert diff_json = open("tests/fixtures/correct_result.txt").read()
