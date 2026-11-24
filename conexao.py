import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def conectar():

    url = os.environ.get('DATABASE_URL', '').strip()
    chave = os.environ.get('SECRET_KEY', '')

    print("DATABASE_URL existe:", bool(url))
    print("Começa com postgresql://:", url.startswith('postgresql://'))
    print("Contém SECRET_KEY:", bool(chave) and chave in url)
    print("Contém espaços:", any(c.isspace() for c in url))

    conexao = psycopg2.connect(
        url,
        connect_timeout=10
    )

    return conexao