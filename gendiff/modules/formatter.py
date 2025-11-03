from .formatters._json import json_
from .formatters._plain import plain
from .formatters._stylish import stylish


def formatter(format: str, tree: list) -> str:
    match format:
        case 'stylish':
            return stylish(tree)
        case 'plain':
            return plain(tree)
        case 'json':
            return json_(tree)
        case _:
            raise ValueError(f'unknown format output: {format}')