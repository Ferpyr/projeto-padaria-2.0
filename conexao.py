import psycopg2

def conectar():
    conexao = psycopg2.connect(
        dbname='banco_padaria',
        user='postgres',
        password='1234',
        port='5432',
        host='127.0.0.1'
    )

    return conexao