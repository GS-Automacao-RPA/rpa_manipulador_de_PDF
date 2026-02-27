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
    file = 'src/bolbnb_20260227_08-56-50.pdf'

    
    with open(file, 'rb') as file_bin:
        pdf = PdfReader(file_bin)
        page = pdf.pages[0]
        text = page.extract_text().split('\n')
        for i in enumerate(text):
            print(i)
        # codigo = pegar_numeros(text[16])
        # data_venc = pegar_numeros(text[30])
        # nome_emp = pegar_maiusculas(text[2])
        # nome_cli = pegar_maiusculas(text[18])
        # print(f"{data_venc}-{nome_emp}-{nome_cli}-{codigo}")
        
      

           

         
 


f27()