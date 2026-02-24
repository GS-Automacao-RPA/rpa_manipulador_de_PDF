from src.utils.relatorio.gravar_registro import gravar_registro
from src.utils.relatorio.medir_tempo import medir_tempo
from src.utils.relatorio.get_token import get_token
from functools import wraps
from sys import exit


def enviar_relatorio(func):
    @wraps(func)
    def wrapper():
        # Cálculo do tempo de execução da função principal.
        report_data: dict = medir_tempo(func)
        # Captura do token.
        token: str = get_token()

        gravar_registro(token, report_data)
        exit()

    return wrapper