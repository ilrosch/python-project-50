import json
import os

import yaml


def _parse(extension: str, data) -> dict:
    match extension:
        case 'json':
            return json.load(data)
        case 'yml' | 'yaml':
            return yaml.load(data, Loader=yaml.Loader)
        case _:
            raise ValueError(f'unknown file format: {extension}')
        

def parse_file(file_path: str) -> dict:
    _, extension = os.path.splitext(file_path)
    file_data = open(file=file_path, mode='r', encoding='utf-8')
    return _parse(extension[1:], file_data)
