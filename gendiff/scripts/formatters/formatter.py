from ._plain import plain
from ._stylish import stylish


def formatter(format: str, tree: list) -> str:
    match format:
        case 'stylish':
            return stylish(tree)
        case 'plain':
            return plain(tree)
        case _:
            return ""