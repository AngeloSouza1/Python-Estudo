from fastapi import FastAPI, Query
from typing import List

app = FastAPI()

# Dicionário com os cursos
cursos = {
    1: {
        "nome": "Dominando o Python",
        "nivel": "básico",
        "formacao": "Python Fundamentos"
    },
    2: {
        "nome": "Automação de Tarefas",
        "nivel": "intermediário",
        "formacao": "Automação"
    },
    3: {
        "nome": "Automação com Selenium",
        "nivel": "intermediário",
        "formacao": "Automação"
    }
}

# Rota com Path Parameter
@app.get("/cursos/formacao/{formacao}")
async def listar_cursos_por_formacao(formacao: str):
    """
    Listar cursos de uma determinada formação usando Path Parameter.
    :param formacao: Nome da formação
    """
    cursos_filtrados = [
        curso for curso in cursos.values() if curso["formacao"] == formacao
    ]
    return cursos_filtrados

# Rota com Query Parameter
@app.get("/cursos")
async def listar_cursos_por_query(nivel: str = Query(None), formacao: str = Query(None)):
    """
    Listar cursos usando Query Parameters.
    :param nivel: Nível do curso (opcional)
    :param formacao: Nome da formação (opcional)
    """
    cursos_filtrados = cursos.values()

    if formacao:
        cursos_filtrados = [
            curso for curso in cursos_filtrados if curso["formacao"] == formacao
        ]

    if nivel:
        cursos_filtrados = [
            curso for curso in cursos_filtrados if curso["nivel"] == nivel
        ]

    return cursos_filtrados
