import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def conectar():
    conexao = psycopg2.connect(
        os.environ['DATABASE_URL'],
        connect_timeout=10
    )

    return conexao
