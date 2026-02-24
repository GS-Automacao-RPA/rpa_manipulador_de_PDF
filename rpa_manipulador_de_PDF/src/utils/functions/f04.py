from PyPDF2 import PdfReader
from tqdm import tqdm
import os
import re

def pegar_numeros(texto: str):
    return ''.join(re.findall(r'\d+', str(texto)))

def nome_unico(caminho):
    if not os.path.exists(caminho):
        return caminho

    base, ext = os.path.splitext(caminho)
    contador = 1
    while True:
        novo = f"{base}_{contador}{ext}"
        if not os.path.exists(novo):
            return novo
        contador += 1


def f04() -> int:
    if not os.path.exists('Arquivos'):
        os.mkdir('Arquivos')

    tot_pags = 0

    prefixos = {
        '0': 'Boleto Adm - ',
        '1': 'Boleto Despesa - '
    }

    print(
        'Digite:\n'
        '0 para definir os boletos como ADM\n'
        '1 para Despesa\n'
        '2 para nenhum\n'
    )

    r = input().strip()
    prefixo = prefixos.get(r, '')

    for arq in [f for f in os.listdir() if f.lower().endswith('.pdf')]:
        condominio = None

        with open(arq, 'rb') as file:
            pdf_reader = PdfReader(file)
            tot_pags += len(pdf_reader.pages)

            for page_pdf in tqdm(pdf_reader.pages, desc=arq):
                texto = page_pdf.extract_text()
                if not texto:
                    continue

                linhas = texto.split('\n')

                for row in linhas:
                    try:
                        if 'CEP:Data Vencimento:' in row:
                            condominio = row[row.rfind(':') + 1:].strip()
                            data_venc = linhas[51]
                            data_venc = pegar_numeros(data_venc)
                            break
                    except:
                        data_venc = linhas[49]
                        data_venc = pegar_numeros(data_venc)
                        continue            
                if condominio:
                    break

        # arquivo já está fechado aqui
        if condominio:
            destino = f"Boleto {condominio} Venc {data_venc}-.pdf"
            destino = nome_unico(destino)
            os.rename(arq, destino)
        else:
            continue
    return tot_pags
