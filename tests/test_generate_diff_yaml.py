from gendiff.generate_diff import generate_diff


def test_generate_diff():
    diff_yml = generate_diff("tests/fixtures/file1.yml", "tests/fixtures/file2.yml")
    assert diff_yml = open("tests/fixtures/correct_result.txt").read()
