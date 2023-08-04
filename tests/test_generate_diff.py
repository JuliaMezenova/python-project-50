from gendiff.generate_diff import generate_diff


def test_generate_diff():
    diff_json = generate_diff("tests/fixtures/file1.json", "tests/fixtures/file2.json")
    true_result_json = open("tests/fixtures/result_json.txt").read()

    assert diff_json == true_result_json
