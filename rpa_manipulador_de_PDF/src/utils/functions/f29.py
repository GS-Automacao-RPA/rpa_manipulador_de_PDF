from PyPDF2 import PdfReader
from tqdm import tqdm
import os
import re


def pegar_numeros(texto: str):
    return ''.join(re.findall(r'\d+', str(texto)))


def pegar_texto(texto: str):
    return ''.join(re.findall(r'[A-Za-zÀ-ÖØ-öø-ÿ ]+', str(texto)))


def f29() -> int:
    files = [f for f in os.listdir() if f.lower().endswith('.pdf')]

    for file in tqdm(files):
        novo_nome = None  # ← importante

        with open(file, 'rb') as file_bin:
            pdf = PdfReader(file_bin)
            rows = pdf.pages[0].extract_text().split('\n')

            for row in rows:
                if 'Boleto de Cobrança' in row:
                    cliente = rows[9].split(':')[-1].strip()
                    cnpj = pegar_numeros(rows[10])

                    novo_nome = f'BOLETO {cliente}-{cnpj}.pdf'
                    break

        if novo_nome:
            os.rename(file, novo_nome)
        else:
            print(
                f'Formato de boleto não reconhecido no arquivo {file}'
            )

    
