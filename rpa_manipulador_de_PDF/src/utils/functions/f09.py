import os
import re
from PyPDF2 import PdfReader, PdfWriter
from tqdm import tqdm


def f09() -> int:
    tot_pags = 0
    pasta_destino = "Recibos"
    os.makedirs(pasta_destino, exist_ok=True)

    # Escolha de separação
    escolha = ''
    while escolha not in ['1', '2']:
        print('-' * 50)
        escolha = input('1: Separar por funcionário.\n'
                        '2: Separar por Lotação.\n'
                        'Escolha: ').strip()

    # Lê todos os PDFs da pasta
    files = [file for file in os.listdir() if file.lower().endswith('.pdf')]
    if not files:
        print(" Nenhum arquivo PDF encontrado na pasta atual.")
        return 0

    for arq in files:
        print(f"\nLendo arquivo: {arq}")
        try:
            with open(arq, 'rb') as file:
                pdf = PdfReader(file)
                tot_pags += len(pdf.pages)

                for i, pag in enumerate(tqdm(pdf.pages,unit="pág")):
                    texto = pag.extract_text()
                    if not texto:
                        print(f"Página {i+1} sem texto legível, ignorada.")
                        continue

                    # Extrair CNPJ
                    cnpj_match = re.search(r'\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}', texto)
                    if not cnpj_match:
                        print(f"Página {i+1}: CNPJ não encontrado.")
                        continue
                    cnpj = re.sub(r'\D', '', cnpj_match.group())

                    # Extrair Lotação
                    lotacao = None
                
                    if not lotacao:
                        linhas = texto.split('\n')
                        if len(linhas) > 14:
                            lotacao = linhas[14].strip()
                        else:
                            lotacao = "SEM_LOTACAO"
                    print(lotacao)

                    # Extrair Nome (somente se separando por funcionário)
                    nome = None
                    if escolha == '1':
                        if not nome:
                            linhas = texto.split('\n')
                            nome = linhas[18]

                    # Monta o nome base do arquivo
                    if escolha == '1':
                        chave = f"{lotacao}-{nome}-{cnpj}"
                    else:
                        chave = f"{lotacao}-{cnpj}"

                    chave = re.sub(r'[<>:"/\\|?*]', '', chave)

                    # Caminho completo do arquivo
                    file_name = os.path.join(pasta_destino, f"{chave}.pdf")

                    # Se já existir arquivo com mesmo nome, adiciona _1, _2, etc.
                    contador = 1
                    while os.path.exists(file_name):
                        file_name = os.path.join(pasta_destino, f"{chave}_{contador}.pdf")
                        contador += 1

                    # Salva página como PDF individual
                    writer = PdfWriter()
                    writer.add_page(pag)
                    with open(file_name, "wb") as output_pdf:
                        writer.write(output_pdf)

                    print(f" Página {i+1} salva como: {os.path.basename(file_name)}")

        except Exception as e:
            print(f" Erro ao processar '{arq}': {e}")

    print(f"\nTotal de páginas processadas: {tot_pags}")
    print(f" Arquivos salvos em: {os.path.abspath(pasta_destino)}")
    return tot_pags
