STEP = 4
SUFFIX_SIZE = 2
REPLACER = ' '


def _get_indent_size(depth: int) -> int:
    return depth * STEP - SUFFIX_SIZE


def _get_indent(count: int) -> str:
    return REPLACER * count


def _get_indent_bracket(count: int) -> str:
    return REPLACER * (count - SUFFIX_SIZE)


def _normalize(node, depth: int) -> str:
    if not isinstance(node, dict):
        if isinstance(node, bool):
            return str(node).lower()
        if node is None:
            return "null"
        return str(node)
    
    indent_size = _get_indent_size(depth)
    indent = _get_indent(indent_size + SUFFIX_SIZE)
    indent_bracket = _get_indent_bracket(indent_size)

    res = (f'{indent}{k}: {_normalize(v, depth + 1)}' for k, v in node.items())
    return '\n'.join(['{', *res, indent_bracket + '}'])
    

def _get_line(depth: int, type: str, key: str, value) -> str:
    indent = _get_indent(_get_indent_size(depth))
    return f'{indent}{type} {key}: {_normalize(value, depth + 1)}'


def stylish(tree: list) -> str:
    def inner(node, depth: int) -> str:
        def iter(n) -> str:
            match n['type']:
                case 'added':
                    return _get_line(depth, '+', n['key'], n['value'])
                case 'deleted':
                    return _get_line(depth, '-', n['key'], n['value'])
                case 'changed':
                    old = _get_line(depth, '-', n['key'], n['value'][0])
                    new = _get_line(depth, '+', n['key'], n['value'][1])
                    return '\n'.join([old, new])
                case 'unchanged':
                    return _get_line(depth, ' ', n['key'], n['value'])
                case 'node':
                    return _get_line(
                        depth, ' ', n['key'], inner(n['children'], depth + 1)
                    )
            return ""
        
        res = map(iter, node)
        indent_bracket = _get_indent_bracket(_get_indent_size(depth))
        return '\n'.join(['{', *res, indent_bracket + '}'])

    return inner(tree, 1)
