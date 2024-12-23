from projeto import app, db
from flask import render_template, request, redirect, url_for
from projeto.lista_filmes import resultado_filmes
from projeto.livro import livro

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
    
    
@app.route('/livros')
def lista_livros():
    return render_template(
        "livros.html", 
        livros=livro.query.all()
    )    

@app.route('/add_livro', methods=["GET", "POST"])
def adiciona_livro():
    nome = request.form.get('nome')
    descricao = request.form.get('descricao')
    valor = request.form.get('valor')
    
    if request.method == 'POST':
        livro_add = livro(
            nome,
            descricao,
            valor
        )
        db.session.add(livro_add)
        db.session.commit()
        return redirect(url_for('lista_livros'))
    return render_template("novo_livro.html")