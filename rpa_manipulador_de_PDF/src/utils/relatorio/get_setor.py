def get_setor() -> str:
    setor = "Geral"
    if setor is None:
        raise Exception('Setor Vazio')
    return setor
