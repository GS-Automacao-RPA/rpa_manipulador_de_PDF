from src.utils.dotenv.get_env_value import get_env_value
import requests


def get_token(tenant_id: str = None, client_id: str = None, client_secret: str = None) -> str:
    if tenant_id is None:
        tenant_id = get_env_value('TENANT_ID', encoded=True)
    if client_id is None:
        client_id = get_env_value('CLIENT_ID', encoded=True)
    if client_secret is None:
        client_secret = get_env_value('CLIENT_SECRET', encoded=True)

    url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"

    data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
        "scope": "https://graph.microsoft.com/.default"
    }

    response = requests.post(url, data=data)
    response.raise_for_status()

    return response.json()["access_token"]
