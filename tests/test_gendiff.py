import os

from gendiff import generate_diff

current_dir = os.path.dirname(os.path.abspath(__file__))


def test_gendiff():
    file_path1_json = os.path.join(current_dir, "test_data", "file1.json")
    file_path2_json = os.path.join(current_dir, "test_data", "file2.json")

    file_path1_yml = os.path.join(current_dir, "test_data", "file1.yml")
    file_path2_yml = os.path.join(current_dir, "test_data", "file2.yml")

    expected_path = os.path.join(current_dir, "test_data", "expected.txt")

    with open(expected_path) as f:
        expected = f.read()
        res_json = generate_diff(file_path1_json, file_path2_json)
        assert res_json == expected
        res_yml = generate_diff(file_path1_yml, file_path2_yml)
        assert res_yml == expected
        res_json_yml = generate_diff(file_path1_json, file_path2_yml)
        assert res_json_yml == expected