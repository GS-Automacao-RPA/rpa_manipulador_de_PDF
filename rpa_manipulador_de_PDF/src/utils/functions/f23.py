from PyPDF2 import PdfReader
from tqdm import tqdm
import os


def f23() -> int:
    files = [file for file in os.listdir() if '.pdf' in file.lower()]
    n_pags = len(files)
    for file in tqdm(files):
        with open(file, 'rb') as file_bin:
            pdf = PdfReader(file_bin)
            page = pdf.pages[0]
            rows = page.extract_text().split('\n')
        nome, cnpj = '---', '---'
        for i, row in enumerate(rows):
            if row.startswith('Email:Inscrição:'):
                nome = rows[i+1][:-18]
                cnpj = ''.join(char for char in rows[i+1][-18:] if char.isnumeric())
                break


        new_path = f'NF {nome}-{cnpj}.pdf'
        os.rename(file, new_path)
    return n_pags

