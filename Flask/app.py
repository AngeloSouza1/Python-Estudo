from flask import Flask, render_template, request
from lista_filmes import resultado_filmes  # Importa a função para buscar filmes dinamicamente

app = Flask(__name__)

conteudos = []
registros = []

# localhost:5000/
@app.route('/', methods=["GET", "POST"])
def principal():
    if request.method == "POST":
        if request.form.get("conteudo"):
            conteudos.append(request.form.get("conteudo"))
            
    return render_template(
        "index.html",
        conteudos=conteudos
    )

@app.route('/diario', methods=["GET", "POST"])
def diario():
    if request.method == "POST":
        if request.form.get("aluno") and request.form.get("nota"):
            aluno = request.form.get("aluno")
            nota = request.form.get("nota")
            registros.append(
                {
                    "aluno": aluno,
                    "nota": nota
                }
            )
    return render_template(
        "sobre.html",
        registros=registros
    )

@app.route('/filmes')
@app.route('/filmes/<tipo>')
def lista_filmes(tipo='Populares'):
    # Busca filmes dinamicamente com base no tipo
    filmes = resultado_filmes(tipo)
    return render_template(
        "filmes.html",
        filmes=filmes,
        tipo=tipo  # Passa o tipo para o template
    )

if __name__ == "__main__":
    app.run(debug=True)
