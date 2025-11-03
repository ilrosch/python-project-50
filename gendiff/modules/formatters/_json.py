import json

  
def json_(tree: list) -> str:
    return json.dumps(obj=tree, indent=2, ensure_ascii=False)
