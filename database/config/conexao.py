import pyodbc
from decouple import config

def conexao_db(db):
    dados_conexao = (
        "Driver={PostgreSQL Unicode};"
        f"Server={config('SERVER')};"
        f"Database={db};"
        f"UID={config('USER_DB')};"
        f"PWD={config('SENHA_DB')};"
        f"Port=5432;"
    )
    print(dados_conexao)

    conexao = pyodbc.connect(dados_conexao)
    return conexao