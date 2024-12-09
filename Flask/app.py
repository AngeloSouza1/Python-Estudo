from flask import Flask, render_template

app = Flask(__name__)

# localhost:5000/
@app.route('/')
def principal():
    conteudos = [
        'Manipulação de Dados',
        'Herança e Templates',
        'Integração de APIs',
        'Banco de Dados',
        'Deploy da App'
    ]
    return render_template(
        "index.html",
        conteudos=conteudos
    )

@app.route('/diario')
def diario():
    diario = {
        "Fulano":5.0,
        "Beltrano":6.0,
        "Teste":7.0,
        "Sicrano":8.5,
        "Rodrigo": 9.0,
        "Fernanda":10.0
    }
    return render_template(
        "sobre.html",
        diario=diario  
    )
