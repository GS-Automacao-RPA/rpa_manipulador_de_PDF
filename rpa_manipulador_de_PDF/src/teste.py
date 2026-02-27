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
    file = 'src/NF - 41069022248405966000135000000000014326020084990796 - Simples Nacional naData deCompetência - 412.pdf'

    
    with open(file, 'rb') as file_bin:
        pdf = PdfReader(file_bin)
        page = pdf.pages[0]
        text = page.extract_text().split('\n')
        for i in enumerate(text):
            print(i)
      
        
      

           

         
 


f27()