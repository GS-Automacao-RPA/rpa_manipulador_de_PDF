def shift_string(texto: str, passo: int = 38) -> str:
    """
    Desloca cada caractere da string pelo valor de 'passo',
    considerando caracteres ASCII imprimíveis (32 a 126).
    """
    inicio = 32   # espaço
    fim = 126     # ~
    tamanho = fim - inicio + 1  # total de caracteres válidos
    resultado = []

    for char in texto:
        codigo = ord(char)
        # Mantém caracteres fora do intervalo.
        if codigo < inicio or codigo > fim:
            resultado.append(char)
            continue

        novo_codigo = inicio + ((codigo - inicio + passo) % tamanho)
        resultado.append(chr(novo_codigo))

    return ''.join(resultado)
