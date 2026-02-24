from src.utils.constants import DOTENV_PATH
from dotenv import load_dotenv
import os


def carregar_env() -> None:
    if not os.path.exists(DOTENV_PATH):
        raise Exception(f'Não foi possível encontrar o arquivo .env: {DOTENV_PATH}')
    load_dotenv(dotenv_path=DOTENV_PATH)
