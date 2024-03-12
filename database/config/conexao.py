import pyodbc
from decouple import config

def conexao_db(db):
    dados_conexao = (
        "Driver={SQL Server};"
        f"Server={config('SERVER')};"
        f"Database={db};"
        f"UID={config('USER_DB')};"
        f"PWD={config('SENHA_DB')};"
        # f"INSTANCE={}"
    )

    conexao = pyodbc.connect(dados_conexao)
    return conexao