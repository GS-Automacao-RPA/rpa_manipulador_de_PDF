from src.utils.get_project_root import get_project_root
from pathlib import Path


VERSION: str = 'V2.1.0'
NOME = 'Manipulador de PDF'
PROJECT_ROOT: Path = get_project_root()  # Pasta raiz do projeto.
DOTENV_PATH: Path = PROJECT_ROOT / 'resources' / '.env'  # Caminho do .env.
SHIFT: int = 38
# Envio do relatório.
SITE_ID: str = 'gsfacilities.sharepoint.com,2ec767bd-f7ca-4070-acd0-3b35e251fa5d,bc2cbdab-1362-445c-a9ee-593055fb9ca7'
LIST_ID: str = '4dd28ff5-b8de-4934-9cdb-703182c4cc19'
