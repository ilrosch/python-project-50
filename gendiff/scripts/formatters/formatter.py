from ._stylish import stylish


def formatter(format: str, tree: list) -> str:
    match format:
        case 'stylish':
            return stylish(tree)
        case _:
            return ""