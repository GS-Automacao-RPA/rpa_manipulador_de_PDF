#CÓDIGO PARA RENOMEAÇÃO DE NFS DE BALNEARIO CAMBURIU QUE CONTÉM APENAS CARACTERES.

from PyPDF2 import PdfReader
import re
import os
from tqdm import tqdm

def f24() -> int :
    arquivos_pdf = [arquivo for arquivo in os.listdir() if ".pdf" in arquivo.lower()]
    num_nfs = len(arquivos_pdf)

    for arquivo in tqdm(arquivos_pdf, total=len(arquivos_pdf)):

        with open(arquivo, "rb") as pdf_nota_fiscal:
            #LEITURA DO TEXTO DO PDF
            pdf_reader = PdfReader(pdf_nota_fiscal)
            page = pdf_reader.pages[0]
            text = page.extract_text()

            #BUSCAR NUMERO DA NOTA
            pos_inicial_nota = text.find("NFS-eNúmero da nota") + len("NFS-eNúmero da nota") + 1
            pos_final_nota = text.find(" - E") + len(" - E")
            num_nota = text[pos_inicial_nota:pos_final_nota]

            #BUSCAR NOME TOMADOR DE SERVICOS
            for razao_social in re.finditer("Nome/Razão Social: ", text):
                pos_inicial_razao_social = razao_social.start()
            pos_inicial_razao_social = pos_inicial_razao_social + len("Nome/Razão Social: ")


            for razao_social in re.finditer("E-mail", text):
                pos_final_razao_social = razao_social.start() - 1
            
            razao_social = text[pos_inicial_razao_social:pos_final_razao_social]

            #BUSCAR CNPJ
            cnpj = text.find("CPF/CNPJ: ") + len("CPF/CNPJ: ")
            cnpj = text[cnpj:cnpj+18]
            cnpj = cnpj.replace("/", "_")

        try:
            novo_nome = os.path.join(f"NF {razao_social} - {cnpj}.pdf")
            novo_nome = os.path.abspath(novo_nome)
            os.rename(arquivo, novo_nome)
        except:
            pass
    
    return num_nfs