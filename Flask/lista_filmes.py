import urllib.request
import json

url = 'https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=8e0c5130f5d00dd74f764af4153b5e6f'

# Faz a requisição à API
resposta = urllib.request.urlopen(url)
dados = resposta.read()
dados_json = json.loads(dados)

# Processa os dados para extrair os campos necessários
filmes = [
    {
        "title": filme.get("title"),
        "backdrop_path": filme.get("backdrop_path"),
        "overview": filme.get("overview"),
        "vote_average": filme.get("vote_average")
    }
    for filme in dados_json.get("results", [])
]
