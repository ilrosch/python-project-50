import os

from gendiff import generate_diff

current_dir = os.path.dirname(os.path.abspath(__file__))


def test_gendiff_json():
    file_path1 = os.path.join(current_dir, "test_data", "file1.json")
    file_path2 = os.path.join(current_dir, "test_data", "file2.json")
    expected_path = os.path.join(current_dir, "test_data", "expected.txt")

    with open(expected_path) as f:
        expected = f.read()
        actual = generate_diff(file_path1, file_path2)
        assert actual == expected