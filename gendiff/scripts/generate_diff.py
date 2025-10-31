from .parse import parse

STEP_SIZE = 2


def generate_diff(file_path1: str, file_path2: str) -> str:
    file_parsed1 = dict(parse(file_path1))
    file_parsed2 = dict(parse(file_path2))

    def inner(data: list, depth: int) -> str:
        file_keys = list(set(data))
        file_keys.sort()

        current_depth = depth + STEP_SIZE
        current_indepent = " " * current_depth
        bracket_depth = " " * depth

        res = []
        for key in file_keys:
            value1 = file_parsed1.get(key, None)
            value2 = file_parsed2.get(key, None)

            if key not in file_parsed1:
                res.append(f"{current_indepent}+ {key}: {value2}")
                continue
            
            if key not in file_parsed2:
                res.append(f"{current_indepent}- {key}: {value1}")
                continue

            if value1 != value2:
                res.append(f"{current_indepent}- {key}: {value1}")
                res.append(f"{current_indepent}+ {key}: {value2}")
                continue

            res.append(f"{current_indepent}  {key}: {value2}")
        
        return '\n'.join(["{", *res, bracket_depth + "}"]).lower()

    return inner([*file_parsed1.keys(), *file_parsed2.keys()], 0)
