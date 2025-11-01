
import os

import pytest

from gendiff.scripts._parse import parse_file


def test_parse_unknown(path_test_dir):
    file_path = os.path.join(path_test_dir, 'test_data', 'unknown.txt')
    with pytest.raises(Exception, match=r".*unknown file format.*"):
        parse_file(file_path)