from pypdf import PdfReader, PdfWriter
import os
import re
from pathlib import Path


def f30() -> int:
    processar_pdf()
    return 0


def pegar_numeros(texto: str):
    return ''.join(re.findall(r'\d+', str(texto)))


def limpar_nome(nome):
    return re.sub(r'[\\/*?:"<>|]', "", nome)


def extrair_informacao(texto: str):
 

    linhas = texto.split('\n')

    try:
        cpf = pegar_numeros(linhas[13])
        nome = linhas[17].strip()
        return f"{nome}_{cpf}"
    except IndexError:
        return None


import os
from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter
from tqdm import tqdm


def processar_pdf():
    files = [f for f in os.listdir() if f.lower().endswith('.pdf')]

    if not files:
        return

    pasta_saida = "Arquivos_Separados"
    Path(pasta_saida).mkdir(exist_ok=True)

    for file in files:
        reader = PdfReader(file)

        # tqdm no lugar do enumerate
        for i in tqdm(range(len(reader.pages)), desc=f"Processando {file}", unit="página"):
            pagina = reader.pages[i]

            writer = PdfWriter()
            writer.add_page(pagina)

            texto = pagina.extract_text()

            if not texto:
                nome_final = f"{Path(file).stem}_pagina_{i+1}_SEM_TEXTO"
            else:
                info = extrair_informacao(texto)

                if info:
                    info = limpar_nome(info)
                    nome_final = info
                else:
                    nome_final = f"{Path(file).stem}_pagina_{i+1}_NAO_IDENTIFICADO"

            caminho_saida = os.path.join(pasta_saida, f"{nome_final}.pdf")

            contador = 1
            while os.path.exists(caminho_saida):
                caminho_saida = os.path.join(
                    pasta_saida,
                    f"{nome_final}_{contador}.pdf"
                )
                contador += 1

            with open(caminho_saida, "wb") as f:
                writer.write(f)