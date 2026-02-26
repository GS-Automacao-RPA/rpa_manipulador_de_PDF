from PyPDF2 import PdfReader
from tqdm import tqdm
import re
import os

def pegar_maiusculas(texto: str) -> str:
    return ''.join(re.findall(r'[A-ZÀ-ÖØ-Þ ]', texto))


def pegar_numeros(texto: str):
    return ''.join(re.findall(r'\d+', str(texto)))

def pegar_texto(texto: str):
    return ''.join(re.findall(r'[A-Za-zÀ-ÖØ-öø-ÿ ]+', str(texto)))

def f27() -> int:
    file = 'src/INFORME RENDIMENTOS CONDOS -69.pdf'

    
    with open(file, 'rb') as file_bin:
        pdf = PdfReader(file_bin)
        page = pdf.pages[0]
        text = page.extract_text().split('\n')
        cpf = text[13]
        cpf = pegar_numeros(cpf)
        nome = text[17]
        print(f'CPF: {cpf}')
        print(f'Nome: {nome}')
      

           

         
 


f27()