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

@app.route('/sobre')
def sobre():
    return render_template("sobre.html")