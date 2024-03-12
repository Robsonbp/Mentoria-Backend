from pydantic import BaseModel
from datetime import datetime, date
from pyodbc import Connection


class Pessoa(BaseModel):
    nome: str
    email: str
    dt_nascimento: date

    def cadastrar_pessoa(self, conexao: Connection):
        cursor = conexao.cursor()
        cursor.execute(f"""
            insert into pessoas (nome, email, dt_nascimento)
            values
            ({self.nome}, {self.email}, {self.dt_nascimento})
        """)


class PessoaList(BaseModel):
    lista: list[Pessoa]


def get_pessoas(conexao: Connection) -> PessoaList:
    cursor = conexao.cursor()
    cursor.execute(f"""
        select * from pessoas
    """)
    tabela_sql = cursor.fetchall()
    pessoas: list = []
    for registro in tabela_sql:
        pessoas.append(
            Pessoa(
                nome=registro.nome,
                email=registro.email,
                dt_nascimento=registro.dt_nascimento
            )
        )
    return PessoaList(lista=pessoas)
