import os


def is_test() -> bool:
    # Verifica apenas se há alguma variável no .env chamada "TESTE".
    return 'TESTE' in os.environ
