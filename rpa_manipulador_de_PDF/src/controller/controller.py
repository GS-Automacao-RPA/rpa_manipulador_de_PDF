from src.utils.relatorio.enviar_relatorio import enviar_relatorio
from src.utils.dotenv.carregar_env import carregar_env
from src.view.menu_opcoes import main_hub
from src.utils.get_json import get_main_msg_json, json_serializer
import json


@enviar_relatorio
def run() -> dict:
    carregar_env()
    n_pages = main_hub()
    report_data = dict()
    json_data = get_main_msg_json

    quantidade: int = n_pages
    log: dict = json_data
    report_data['quantidade'] = quantidade
    report_data['taxa_sucesso'] = 1
    report_data['log'] = json.dumps(log ,default=json_serializer)
    return report_data
