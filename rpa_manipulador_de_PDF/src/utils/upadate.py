from io import BytesIO
from time import sleep
import requests
import zipfile


# Configurações do repositório
OWNER = "GS-Automacao"
REPO = "Manipulador-PDF"

def baixar_release_mais_recente():
    url_api = f"https://api.github.com/repos/{OWNER}/{REPO}/releases/latest"

    print(f"Consultando a versão mais recente do robô...")
    response = requests.get(url_api)
    if response.status_code != 200:
        raise Exception(f"Erro ao consultar release: {response.status_code}")

    release = response.json()
    tag = release['tag_name']
    print(f"Versão encontrada: {tag}")

    # Procura por arquivos .zip ou .exe nos assets
    for asset in release['assets']:
        nome = asset['name']
        download_url = asset['browser_download_url']

        if nome.endswith(".zip") or nome.endswith(".exe"):
            print(f"Baixando: {nome}")
            r = requests.get(download_url)
            if r.status_code != 200:
                raise Exception("Erro ao baixar o arquivo")

            if nome.endswith(".zip"):
                print("Extraindo conteúdo do ZIP...")
                with zipfile.ZipFile(BytesIO(r.content)) as z:
                    z.extractall("..")
                print('Sucesso!')
                sleep(3)
            else:
                with open(nome, "wb") as f:
                    f.write(r.content)
                print(f"Executável salvo como: {nome}")
            return

    print("Nenhum arquivo .zip ou .exe encontrado na release mais recente.")


if __name__ == "__main__":
    try:
        baixar_release_mais_recente()
    except Exception as e:
        print(f"Erro: {e}")
