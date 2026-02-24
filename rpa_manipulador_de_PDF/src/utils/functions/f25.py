from email.mime import text
from PyPDF2 import PdfReader
from tqdm import tqdm
import os
import re

def pegar_numeros(texto: str):
    return ''.join(re.findall(r'\d+', str(texto)))

def pegar_texto(texto: str):
    return ''.join(re.findall(r'[A-Za-zÀ-ÖØ-öø-ÿ ]+', str(texto)))

def pegar_maiusculas(texto: str) -> str:
    return ''.join(re.findall(r'[A-ZÀ-ÖØ-Þ ]', texto))

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


def f25() -> int:
    files = [file for file in os.listdir() if file.lower().endswith('.pdf')]
    palavras_ignoradas = ['E-mail', 'Email']
    n_arqs = len(files)
    for file in tqdm(files):
        with open(file, 'rb') as file_bin:
            pdf = PdfReader(file_bin)
            rows = pdf.pages[0].extract_text().split('\n')
        for row in rows:
            if 'Data de Emissão' in row:
                num_nf = row.split()[0]
                break
        for row in rows[::-1]:
            if 'Nome/Razão Social' in row:
                nome_cliente = row[18:]
                nome_cliente = nome_cliente.translate(str.maketrans({'/': '', '\\': '', '|': ''}))
                novo_nome = f'NF {nome_cliente}-{num_nf}.pdf'
                os.rename(file, novo_nome)
                break
        
            elif 'Número da Nota' in rows:
                n_nota = rows[1]
                n_nota = pegar_numeros(n_nota)
                nome_cliente = rows[19].split(':')
                nome_cliente = nome_cliente[1:]
                nome_cliente = pegar_texto(nome_cliente)
                novo_nome = f'NF {nome_cliente}-{n_nota}.pdf'
                os.rename(file, novo_nome)
                break

            elif 'DANFSe v1.0' in rows:
                n_nota = pegar_numeros(rows[10])
                cliente = (rows[37])
                cliente = cliente.replace('E-mail', '')
                cnpj = pegar_numeros(rows[33])
                novo_nome = f'NF - {n_nota}-{cliente}-{cnpj}.pdf'
                novo_nome = gerar_nome_unico(novo_nome)
                os.rename(file, novo_nome)
                break
            else:
                print('Arquivo não reconhecido, por favor, entrar em contato com a equipe de automação!')