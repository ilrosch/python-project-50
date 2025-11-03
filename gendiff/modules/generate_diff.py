import sys

from .build_diff_tree import build_diff_tree
from .formatter import formatter
from .parse import parse_file


def generate_diff(file_path1: str, file_path2: str, format: str = "stylish"):
    try:
        data_a = parse_file(file_path1)
        data_b = parse_file(file_path2)
        diff_tree = build_diff_tree(data_a, data_b)
        result = formatter(format, diff_tree)
        print(result)
        sys.exit(0)
    except Exception as err:
        print(err)
        sys.exit(1)
