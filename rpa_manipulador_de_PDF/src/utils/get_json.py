import json
from src.utils.dicionario import NAMES

def get_main_msg_json() -> str:
    return json.dumps(NAMES, ensure_ascii=False, indent=4)

def json_serializer(obj):
    if callable(obj):
        return obj.__name__
    raise TypeError(f"Tipo não serializável: {type(obj)}")