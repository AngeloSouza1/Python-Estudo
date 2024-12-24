from fastapi import FastAPI

app = FastAPI()

# localhost:8000/
@app.get('/')
def inicio():
    return {"Mensagem": "Olá mundo!"}
