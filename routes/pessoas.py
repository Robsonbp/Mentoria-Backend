from fastapi import APIRouter
from fastapi import Body
from fastapi import HTTPException
import pyodbc
from decouple import config

from database.config.conexao import conexao_db
from schemas import pessoas


router = APIRouter(prefix="/pessoas")

@router.get("/")
def get_pessoas():
    try:
        conexao = conexao_db(config("DATABASE"))
        pessoas_list: pessoas.PessoaList = pessoas.get_pessoas(conexao=conexao)
        return pessoas_list
    except Exception as err:
        print(err)
        return HTTPException(status_code=400, detail=str(err))

@router.get("/{id_pessoa}")
def get_pessoa(id_pessoa: int):
    try:
        conexao = conexao_db(config("DATABASE"))
        pessoa: pessoas.Pessoa = pessoas.get_pessoa(conexao=conexao, id=id_pessoa)
        return pessoa
    except Exception as err:
        print(err)
        return HTTPException(status_code=400, detail=str(err))