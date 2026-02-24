def get_nome_automacao() -> str:
    nome = "Manipulador de PDF"
    if nome is None:
        raise Exception('Nome Vazio')
    return nome
