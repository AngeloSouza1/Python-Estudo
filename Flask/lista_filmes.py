import urllib.request
import json

url = 'https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=8e0c5130f5d00dd74f764af4153b5e6f'

resposta = urllib.request.urlopen(url)

dados = resposta.read()

dados_json = json.loads(dados)

# print(dados_json['results'])