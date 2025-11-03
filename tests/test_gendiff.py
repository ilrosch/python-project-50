import os

import pytest

from gendiff import generate_diff


@pytest.mark.parametrize("formatter", ["stylish", "plain", "json"])
@pytest.mark.parametrize("ext", ["json", "yml", "yaml"])
def test_gendiff_formats(path_test_dir, read_expected_file, ext, formatter):
    file_path1 = os.path.join(path_test_dir, "test_data", f"file1.{ext}")
    file_path2 = os.path.join(path_test_dir, "test_data", "file2.json")
    actual = generate_diff(file_path1, file_path2, formatter)
    expected = read_expected_file(formatter)
    assert actual == expected