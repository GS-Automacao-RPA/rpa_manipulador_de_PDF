import os
from PyPDF2 import PdfReader
from tqdm import tqdm
import re

def gerar_nome_unico(nome_base: str) -> str:
    if not os.path.exists(nome_base):
        return nome_base

    nome, ext = os.path.splitext(nome_base)
    contador = 1

    while True:
        novo_nome = f"{nome} ({contador}){ext}"
        if not os.path.exists(novo_nome):
            return novo_nome
        contador += 1
        
def pegar_numeros(texto: str):
    return ''.join(re.findall(r'\d+', str(texto)))

def pegar_texto(texto: str):
    return ''.join(re.findall(r'[A-Za-zÀ-ÖØ-öø-ÿ ]+', str(texto)))

def pegar_maiusculas(texto: str) -> str:
    return ''.join(re.findall(r'[A-ZÀ-ÖØ-Þ ]', texto))

def f27() -> int:
    files = [f for f in os.listdir() if f.lower().endswith('.pdf')]

    for file in tqdm(files):

        novo_nome = None

        with open(file, 'rb') as file_bin:
            pdf = PdfReader(file_bin)
            page = pdf.pages[0]
            text = page.extract_text().split('\n')

            for row in text:
                if row.startswith('DANFSe v1.0'):
                    cliente = text[38]
                    cliente = cliente.replace('E-mail', '')
                    n_nota = pegar_numeros(text[11])
                    cnpj = pegar_numeros(text[34])
                    nome_base = f'NF - {n_nota} - {cliente} - {cnpj}.pdf'
                    novo_nome = gerar_nome_unico(nome_base)
                    break

        if novo_nome:
            os.rename(file, novo_nome)

