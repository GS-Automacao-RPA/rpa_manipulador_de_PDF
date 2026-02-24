from src.utils.constants import LIST_ID, SITE_ID, VERSION
from src.utils.relatorio.get_nome_automacao import get_nome_automacao
from src.utils.relatorio.get_setor import get_setor
from src.utils.relatorio.is_test import is_test
from datetime import datetime, UTC
import requests
import getpass


def gravar_registro(token: str, report_data: dict) -> None:
    nome_automacao = get_nome_automacao()
    data = datetime.now(UTC).isoformat().replace("+00:00", "Z")
    quantidade = report_data.get('quantidade', 0)
    tempo_exec = report_data.get('tempo_de_execucao', 0)
    taxa_sucesso = round(report_data.get('taxa_sucesso', 0), 2)
    setor = get_setor()
    versao = VERSION
    teste = is_test()
    usuario = getpass.getuser()
    sucesso = report_data.get('sucesso', False)
    log = report_data.get('log', '')


    url = f"https://graph.microsoft.com/v1.0/sites/{SITE_ID}/lists/{LIST_ID}/items"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    payload = {
        "fields": {
            "Title": nome_automacao,  # Título
            "Data": data,  # Data
            "Quantidade": quantidade,  # Quantidade
            "Tempodeexecu_x00e7__x00e3_o": tempo_exec,  # Tempo de execução
            "Taxadesucesso": taxa_sucesso,  # Taxa de sucesso
            "Setor": setor,  # Setor
            "Vers_x00e3_odoprojeto": versao,  # Versão do projeto
            "Teste": teste,  # Teste
            "Usu_x00e1_rio": usuario,  # Usuário
            "Sucesso": sucesso,  # Resultado da execução
            "Logdeexecu_x00e7__x00e3_o": log  # Logs
        }
    }

    r = requests.post(url, headers=headers, json=payload)

    if r.status_code not in (200, 201):
        print(f'Erro ao gravar registro: {r.status_code}')
        input(r.text)
        return None
