from PyPDF2 import PdfReader, PdfWriter
from tqdm import tqdm
import os


def f26() -> int:
    # Cria a pasta de destino dos recibos
    if not os.path.exists('Arquivos'):
        os.mkdir('Arquivos')
    tot_pags: int = 0
    prefixos = {
        '0': 'Boleto Adm -',
        '1': 'Boleto Despesa - '
    }
    print('Digite '
          '0 para definir os boletos como ADM;'
          '1 para Despesa;'
          '2 para nenhum.\n')
    r = input()
    prefixo = prefixos.get(r, '')

    for i, file in enumerate(tqdm([file for file in os.listdir() if file.lower().endswith('.pdf')])):
        tot_pags += 1
        with open(file, 'rb') as b:
            pdf = PdfReader(b)
            writer = PdfWriter()
            for page in pdf.pages:
                writer.add_page(page)
            page = pdf.pages[0]
            rows = page.extract_text().split('\n')
        for row in rows[::-1]:
            if row.startswith('Pagador '):
                cnpj = row.split()[-1]
                cnpj = ''.join(char for char in cnpj if char.isnumeric())
                condominio = ' '.join(row.split()[1:-2])
                break
        else:
            cnpj = ''
            condominio = f'não encontrado{i}'

        nome_arq = f'Arquivos/{prefixo}{condominio}-{cnpj}.pdf'
        with open(nome_arq, 'wb') as output:
            writer.write(output)
    return tot_pags

