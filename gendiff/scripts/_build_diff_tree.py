def build_diff_tree(a: dict, b: dict) -> list[dict]:
    all_keys = sorted(a.keys() | b.keys())
    
    def inner(key: str) -> dict:
        if key not in a:
            return {'type': 'added', 'key': key, 'value': b[key]}
        
        if key not in b:
            return {'type': 'deleted', 'key': key, 'value': a[key]}
        
        v_a, v_b = a[key], b[key]

        if isinstance(v_a, dict) and isinstance(v_b, dict):
            return {
                'type': 'node',
                'key': key,
                'children': build_diff_tree(v_a, v_b),
            }
        
        if v_a != v_b:
            return {'type': 'changed', 'key': key, 'value': (v_a, v_b)}
        
        return {'type': 'unchanged', 'key': key, 'value': v_a}

    return list(map(inner, all_keys))