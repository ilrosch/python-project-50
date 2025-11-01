import os

from ._build_diff_tree import build_diff_tree
from ._parse import parse_file
from .formatters.formatter import formatter


def generate_diff(file_path1: str, file_path2: str, format: str):
    try:
        data_a = parse_file(file_path1)
        data_b = parse_file(file_path2)
        diff_tree = build_diff_tree(data_a, data_b)
        return formatter(format, diff_tree)
    except Exception as err:
        print(err)
        os._exit(1)
