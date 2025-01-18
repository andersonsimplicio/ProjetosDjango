import os
from dotenv import load_dotenv
from pathlib import Path
from dotenv import dotenv_values
# Configurar o caminho do .env
BASE_DIR = Path(__file__).resolve().parent
dotenv_path = BASE_DIR / '.env'

# Carregar o arquivo .env
load_dotenv(dotenv_path=dotenv_path)

def test_env_variables():
    # Verificar se as variáveis foram carregadas corretamente
    config = dotenv_values(".env") 
    print(config)
    load_dotenv()
    print("SECRET_KEY:", os.getenv("SECRET_KEY"))
    secret_key = os.getenv('SECRET_KEY')
    
    debug = os.getenv('DEBUG')

    assert secret_key is not None, "SECRET_KEY não foi carregado do arquivo .env"
    assert debug is not None, "DEBUG não foi carregado do arquivo .env"
    assert debug in {'0', '1'}, "DEBUG deve ser '0' ou '1'"