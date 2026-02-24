from PyPDF2 import PdfReader, PdfWriter
from tqdm import tqdm
import pandas as pd
import os


def f06() -> int:
    def get_tabela() -> pd.DataFrame:
        # Encontra a tabela com a relação de lotação->CNPJ.
        files = [file for file in os.listdir() if '.csv' in file]
        if len(files) != 1:
            return pd.DataFrame()
        return pd.read_csv(files[0], header=None, sep=';', encoding='latin1', names=['cod', 'nome', 'cnpj', 'tomador'])

    tot_pags = 0
    df = get_tabela()
    tem_relacao = len(df) > 0
    # Cria a pasta de destino dos recibos
    if not os.path.exists('Arquivos'):
        os.mkdir('Arquivos')

    for arq in [file for file in os.listdir() if '.pdf' in file]:
        with open(arq, 'rb') as file:
            # Cria um objeto PdfFileReader para ler o conteúdo do arquivo PDF
            pdf_reader = PdfReader(file)
            tot_pags += len(pdf_reader.pages)
            pdf_writer = PdfWriter()
            lotacao = ''
            i = 0
            # print(len(pdf_reader.pages))
            if 'Estabelecimento:' in pdf_reader.pages[0].extract_text().split('\n')[4]:
                i = 1

            #INICIO BLOCO DE TESTES
            for page_pdf in tqdm(pdf_reader.pages):
                page = page_pdf.extract_text().split('\n')
                tipo = ' '.join(page[0].split()[:3])
                diferenca = page[3]
                
                # print(tipo)

                # Verifica se já há umas pasta para o tipo
                if not os.path.exists(f'Arquivos/{tipo}'):
                    os.mkdir(f'Arquivos/{tipo}')

                if diferenca == "Licenciado para: ":
                    # Verifica o tipo de arquivo
                    if tipo == 'Folha de Pagamento':
                        lotacao_nova = page[17+i] 
                    elif tipo == 'Listagem de Férias':
                        lotacao_nova = page[16+i] 
                    elif tipo == 'Listagem de Rescisão':
                        lotacao_nova = page[16+i] 

                else: 
                    if tipo == 'Folha de Pagamento':
                        lotacao_nova = page[14+i] 
                    elif tipo == 'Listagem de Férias':
                        lotacao_nova = page[13+i] 
                    elif tipo == 'Listagem de Rescisão':
                        lotacao_nova = page[13+i]
                

                # Verifica se está na página de resumo ou se a lotacao for a mesma, se sim,
                # junta as páginas, caso contrário, salva o arquivo atual e cria um pdf novo.
                # if ('Total Geral' in lotacao_nova) or (lotacao_nova != lotacao):
                
                if (lotacao_nova != lotacao):
                    if pdf_writer.pages:
                        cnpj = ''
                        if tem_relacao:
                            result = df[df['nome'] == lotacao]['cnpj']
                            if len(result) == 1:
                                cnpj = result[0]
                        file_name = f'Arquivos/{tipo}/{lotacao.replace('/', '')}-{cnpj}.pdf'

                        with open(file_name, 'wb') as output_file:
                            pdf_writer.write(output_file)
                        pdf_writer = PdfWriter()
                    lotacao = lotacao_nova
                    if ('Total Geral' not in lotacao_nova):
                        pdf_writer.add_page(page_pdf)
                else:
                    pdf_writer.add_page(page_pdf)
                # pdf_writer.add_page(page_pdf)
            #FIM BLOCO DE TESTES
    return tot_pags
