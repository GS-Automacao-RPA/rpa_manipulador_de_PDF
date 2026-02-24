from typing import Callable
from time import time


def medir_tempo(func: Callable, cd: int = 2) -> dict:
    """
    Calcula o tempo de execução de uma função.

    Parâmetros:
    func (Callable): A função que terá o tempo medido.
    cd (int): Total de casas decimais que serão consideradas.

    Retorna:
    (float) O tempo de execução da função.
    """
    tempo_inicio: float = time()
    report_data: dict = func()  # Executa a função.
    tempo_fim: float = time()
    # Cálculo do tempo de execução.
    report_data['tempo_de_execucao'] = round(tempo_fim - tempo_inicio, cd)

    return report_data
