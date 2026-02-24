from pathlib import Path
import sys


def get_project_root() -> Path:
    """
    Retorna o diretório base do projeto (onde está o src/)
    """
    if getattr(sys, 'frozen', False):
        return Path(sys.executable).parent
    return Path(__file__).resolve().parents[1]
