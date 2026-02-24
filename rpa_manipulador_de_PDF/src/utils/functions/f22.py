from PyPDF2 import PdfReader
from tqdm import tqdm
import os
import re

def pegar_maiusculas(texto: str) -> str:
    return ''.join(re.findall(r'[A-ZÀ-ÖØ-Þ ]', texto))


def pegar_numeros(texto: str):
    return ''.join(re.findall(r'\d+', str(texto)))

def pegar_texto(texto: str):
    return ''.join(re.findall(r'[A-Za-zÀ-ÖØ-öø-ÿ ]+', str(texto)))

def f22() -> int:
    files = [file for file in os.listdir() if '.pdf' in file.lower()]
    n_pags = len(files)
    for file in tqdm(files):
        with open(file, 'rb') as file_bin:
            pdf = PdfReader(file_bin)
            page = pdf.pages[0]
            rows = page.extract_text().split('\n')
        # Variável indicadora, para capturar apenas o segundo logradouro.
        segundo_logradouro = False
        for row in rows:
            if 'Logradouro:' in row:
                if segundo_logradouro:
                    cnpj = ''.join(char for char in row[11:26] if char.isnumeric()) 
                    nome = ''.join(char for char in row[29:] if not char.isnumeric())

                    new_path = f'NF {nome}-{cnpj}.pdf'
                    os.rename(file, new_path)
                    break
            elif "Número da Nota" in row:
                n_nota = rows[1]
                cliente = rows[14]
                cliente = cliente.split()
                cliente = pegar_texto(cliente)
                cliente = pegar_maiusculas(cliente)
                partes = cliente.split()
                partes[0] = partes[0][1:]
                cliente = ' '.join(partes)
                cnpj = pegar_numeros(rows[14])
                novo_nome = f'NF - {n_nota} - {cliente} - {cnpj}.pdf'
                os.rename(file, novo_nome)
                
                break
            else:
                print("Arquivo não reconhecido, por favor, entrar em contato com a equipe de automação!")
                    
            
    return n_pags
