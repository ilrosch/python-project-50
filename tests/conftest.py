import os

import pytest


@pytest.fixture
def path_test_dir():
    return os.path.dirname(os.path.abspath(__file__))


@pytest.fixture
def expected_stylish_file(path_test_dir):
    file_path = os.path.join(path_test_dir, 'test_data', 'expected_stylish.txt')
    with open(file=file_path, mode='r', encoding='utf-8') as f:
        return f.read()
