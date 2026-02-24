from PyPDF2 import PdfReader
from tqdm import tqdm
import os


def f15() -> int:
    files = [file for file in os.listdir() if '.pdf' in file.lower()]
    n_pags = len(files)
    prefixos = {
        '0': 'Adm',
        '1': 'Despesa'
    }
    print('Digite '
          '0 para definir as NFs como Adm;'
          '1 para Despesa;'
          '2 para nenhum.\n')
    r = input()
    prefixo = prefixos.get(r, '')
    for file in tqdm(files):
        with open(file, 'rb') as file_bin:
            pdf = PdfReader(file_bin)
            page = pdf.pages[0]
            rows = page.extract_text().split('\n')
            # print(rows)
            
        # for i, row in enumerate(rows):
        #     if 'Competência' in row:
        #         nome = row[:row.find('Competência')]
        #         print(nome)
        #     elif row.startswith('Insc.Municipal'):
        #         cnpj = ''.join(char for char in rows[i+1] if char.isnumeric())
        #         print(cnpj)
        #         break

        cnpj = rows[-1][:18].replace(".", "").replace("/", "").replace("-", "")
        nome = rows[-3][rows[-3].find("Endereço")+len("Endereço"):]
        # print(cnpj)
        # print(nome)

        new_path = f'NF {prefixo} {nome} - {cnpj}.pdf'
        os.rename(file, new_path)

    return n_pags
