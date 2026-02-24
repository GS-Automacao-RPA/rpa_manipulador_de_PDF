from PyPDF2 import PdfReader
from tqdm import tqdm
import re
import os

def pegar_numeros(texto: str):
    return ''.join(re.findall(r'\d+', str(texto)))

def f28():
    files =  [file for file in os.listdir() if file.lower().endswith('.pdf')]
    n_arqs = len(files)
    for file in tqdm(files):
        with open(file, 'rb') as file_bin:
            pdf = PdfReader(file_bin)
            page = pdf.pages[0]
            text = page.extract_text().split()
            
            data_antiga = text[15].split('/')
            data_antiga = pegar_numeros(data_antiga)
            data_nova = data_antiga[2:]
            nome_antigo = text[100:104]
            nome_novo = ' '.join(nome_antigo)
            
        nome_arquivo = f'NF {data_nova} - {nome_novo} - 0000000.pdf'
        os.rename(file, nome_arquivo)
    
