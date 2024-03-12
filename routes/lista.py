from fastapi import APIRouter
from fastapi import Body
from fastapi import HTTPException
import pyodbc
from decouple import config

from database.config.conexao import conexao_db
from schemas import pessoas


router = APIRouter(prefix="/lista")

@router.get("/")
def get_lista():
    try:
        conexao = conexao_db(config("DATABASE"))
        pessoas_list: pessoas.PessoaList = pessoas.get_pessoas(conexao=conexao)
        return pessoas_list
    except Exception as err:
        print(err)
        return HTTPException(status_code=400, detail=str(err))
