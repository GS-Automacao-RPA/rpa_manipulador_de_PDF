from src.utils.dotenv.shift_string import shift_string
from src.utils.constants import SHIFT
import os


def get_env_value(key: str, encoded: bool = False) -> str:
    value = os.getenv(key, '')
    if encoded:
        return shift_string(texto=value, passo=SHIFT)
    return value
