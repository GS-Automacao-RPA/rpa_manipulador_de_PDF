import requests


def check_update(VERSION: str):
    last_version = get_last_version()
    if type(last_version) == str:
        if VERSION != get_last_version():
            print('Nova versão disponível!')
            print(
                'Para baixar a nova versão, feche e exclua este arquivo (main.exe) e execute o arquivo "download_last_version" dentro da pasta "configs".')
            input('Para continuar utilizando esta versão, pressione Enter')

def get_last_version():
    OWNER = "GS-Automacao-RPA"
    REPO = "rpa_manipulador_de_PDF"
    url_api = f"https://api.github.com/repos/{OWNER}/{REPO}/releases/latest"
    try:
        response = requests.get(url_api)
        if response.status_code != 200:
            raise Exception(f"Erro ao consultar release: {response.status_code}")
    except:
        pass
    release = response.json()
    tag = release['tag_name']
    return tag
