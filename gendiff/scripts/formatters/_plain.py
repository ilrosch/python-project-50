def _normalize(node) -> str:
    if node is None:
        return 'null'
    if isinstance(node, bool):
        return str(node).lower()
    if isinstance(node, dict):
        return '[complex value]'
    if isinstance(node, str):
        return f"'{node}'"
    return str(node)


def plain(tree: list) -> str:
    def iter(node, acc=''):
        acc += f'.{node['key']}'
        match node['type']:
            case 'node':
                res = map(lambda n: iter(n, acc), node['children'])
                filtered = filter(lambda n: n != '', res)
                return '\n'.join([*filtered])
            case 'added':
                new = _normalize(node['value'])
                return f"Property '{acc[1:]}' was added with value: {new}"
            case 'deleted':
                return f"Property '{acc[1:]}' was removed"
            case 'changed':
                old = _normalize(node['value'][0])
                new = _normalize(node['value'][1])
                return f"Property '{acc[1:]}' was updated. From {old} to {new}"
        return ''
    res = map(iter, tree)
    return '\n'.join([*res])