from fastapi import FastAPI

app = FastAPI()

# Dicionário Jogadores
jogadores = {
    1:{
        "nome": "Dudu",
        "idade": 30,
        "time": "Palmeiras"
    },
    2:{
        "nome": "Vinícius JR",
        "idade": 28,
        "time": "Real Madrid"
    },
    3:{
        "nome": "Raphael Veiga",
        "idade": 29,
        "time": "Palmeiras"
    }
}

# localhost:8000/
@app.get('/')
def inicio():
    return {"Mensagem": "Olá mundo!"}

@app.get('/jogadores')
def lista_jogadores():
    return jogadores

# Path Parameter
# <http://127.0.0.1:8000/jogadores/1>
# <http://127.0.0.1:8000/jogadores/2>
@app.get('/busca-jogador-id/{jogador_id}')
def busca_jogador_id(jogador_id: int):
    return jogadores[jogador_id]