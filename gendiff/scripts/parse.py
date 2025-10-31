import json
import os

import yaml


def _load_json(file_path: str):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def _load_yml(file_path: str):
    with open(file_path, 'r', encoding='utf-8') as f:
        return yaml.load(f, Loader=yaml.Loader)


PARSERS = {
    'json': _load_json,
    'yml': _load_yml,
    'yaml': _load_yml,
}


def parse(file_path: str) -> str:
    _, extension = os.path.splitext(file_path)
    parser = PARSERS.get(extension[1:], None)
    if parser is None:
        raise Exception("ops")
    return parser(file_path)
