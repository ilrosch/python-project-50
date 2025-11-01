import os

import pytest


@pytest.fixture
def path_test_dir():
    return os.path.dirname(os.path.abspath(__file__))


@pytest.fixture
def read_expected_file(path_test_dir):
    def read_file(f):
        file_path = os.path.join(path_test_dir, 'test_data', f'expected_{f}.txt')  # noqa: E501
        with open(file=file_path, mode='r', encoding='utf-8') as f:
            return f.read()
    return read_file