from pydantic import BaseModel
from datetime import datetime, date
from pyodbc import Connection
from typing import Optional


class Pessoa(BaseModel):
    id: Optional[int] = 0
    nome: str
    email: str
    dt_nascimento: date

    def cadastrar_pessoa(self, conexao: Connection):
        cursor = conexao.cursor()
        cursor.execute(f"""
            insert into public."Pessoas" (nome, email, dt_nascimento)
            values
            ({self.nome}, {self.email}, {self.dt_nascimento})
        """)


class PessoaList(BaseModel):
    pessoas: list[Pessoa]


def get_pessoas(conexao: Connection) -> PessoaList:
    cursor = conexao.cursor()
    cursor.execute(f"""
        select * from public."Pessoas"
    """)
    tabela_sql = cursor.fetchall()
    pessoa_ls: list = []
    for registro in tabela_sql:
        pessoa_ls.append(
            Pessoa(
                id=registro.id,
                nome=registro.nome,
                email=registro.email,
                dt_nascimento=registro.dt_nascimento
            )
        )
    return PessoaList(pessoas=pessoa_ls)


def get_pessoa(conexao: Connection, id: int) -> Pessoa:
    cursor = conexao.cursor()
    cursor.execute(f"""
        select * from pessoas
        where id = {id}
    """)
    tabela_sql = cursor.fetchall()
    pessoa_ls: list = []
    for registro in tabela_sql:
        pessoa_ls.append(
            Pessoa(
                id=registro.id,
                nome=registro.nome,
                email=registro.email,
                dt_nascimento=registro.dt_nascimento
            )
        )
    return PessoaList(pessoas=pessoa_ls)