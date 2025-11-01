import os

import pytest

from gendiff import generate_diff


@pytest.mark.parametrize('format', ['json', 'yml', 'yaml'])
def test_gendiff_stylish(path_test_dir, expected_stylish_file, format):
    file_path1 = os.path.join(path_test_dir, 'test_data', f'file1.{format}')
    file_path2 = os.path.join(path_test_dir, 'test_data', 'file2.json')
    actual = generate_diff(file_path1, file_path2, 'stylish')
    assert actual == expected_stylish_file
