from pypdf import PdfReader, PdfWriter
import os
import re
from pathlib import Path
from tqdm import tqdm
from datetime import datetime


def f31() -> int:
    processar_pdf()
    return 0


def pegar_maiusculas(texto: str) -> str:
    return ''.join(re.findall(r'[A-ZÀ-ÖØ-Þ ]', texto))


def pegar_numeros(texto: str):
    return ''.join(re.findall(r'\d+', str(texto)))


def limpar_nome(nome):
    return re.sub(r'[\\/*?:"<>|]', "", nome)


def extrair_informacao(linhas: list[str]):
    try:
        # As variaveis abaixo apresentam algum misterio, pois as linhas não correspondem
        # ao que se espera, mas são as linhas corretas para extrair as informações necessárias.

        codigo = pegar_numeros(linhas[24]).strip()
        data_bruta = (linhas[41]).strip()
        data_venc = datetime.strptime(data_bruta, "%d/%m/%Y").strftime("%d-%m-%Y")
        nome_emp = (linhas[2]).strip()
        nome_cli = pegar_maiusculas(linhas[26]).strip()

        return f"{data_venc}-{nome_emp}-{nome_cli}-{codigo}"

    except (IndexError, TypeError):
        return None


def processar_pdf():
    files = [f for f in os.listdir() if f.lower().endswith('.pdf')]

    if not files:
        return

    pasta_saida = "Arquivos_Separados"
    Path(pasta_saida).mkdir(exist_ok=True)

    for file in files:

        with open(file, 'rb') as file_bin:
            pdf = PdfReader(file_bin)

            for i in tqdm(range(len(pdf.pages)), desc=f"Processando {file}", unit="página"):

                page = pdf.pages[i]
                writer = PdfWriter()
                writer.add_page(page)

                texto = page.extract_text()

                if not texto:
                    nome_final = f"{Path(file).stem}_pagina_{i+1}_SEM_TEXTO"
                else:
                    linhas = texto.split('\n')
                    info = extrair_informacao(linhas)

                    if info:
                        nome_final = limpar_nome(info)
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

                with open(caminho_saida, "wb") as f_out:
                    writer.write(f_out)