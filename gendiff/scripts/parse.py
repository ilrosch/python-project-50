import json


def parse(file_path: str) -> str:
    return json.load(open(file_path))