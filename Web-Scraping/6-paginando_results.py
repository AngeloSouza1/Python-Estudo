import os
import requests
from collections import Counter
from dotenv import load_dotenv
import pandas as pd

# Carregar variáveis do arquivo .env
load_dotenv()

# Acessar variáveis de ambiente
access_token = os.getenv("API_TOKEN")

# 1 - Utilizando Access Token
headers = {
    'Authorization': 'Bearer ' + access_token,
    'X-GitHub-Api-Version': '2022-11-28'
}

# 2 - Mapeando Informações 
base_api = 'https://api.github.com'
owner = 'AngeloSouza1'
url = f'{base_api}/users/{owner}/repos'

# 3 - Organizando os Dados
repos_list = []
for page_num in range(1, 3):
    try:
        url_page = f'{url}?page={page_num}'
        response = requests.get(url_page, headers=headers)
        repos_list.append(response.json())
    except Exception as e:
        repos_list.append(None)
        print(f"Erro ao buscar página {page_num}: {e}")

# print(len(repos_list))
# print(len(repos_list)) # Primeira página
# print(len(repos_list[0])) # Na primeira página tem 30 projetos

# 4 - Filtrando Resultados
# print(repos_list[0][2]) # página - repositório
# print(repos_list[0][2]['name']) # página - repositório

# 5 - Pegando apenas o nome
name_repos = []
for page in repos_list:
    for repo in page:
        name_repos.append(repo['name'])
        
print(name_repos[:10]) # pega os 10 primeiros repositórios
print(len(name_repos))

# 6 - Pegando a linguagem dos repositórios
# print(repos_list[1][1]['language'])
lang_repos = []
for page in repos_list:
    for repo in page:
        lang_repos.append(repo['language'])

# print(len(lang_repos))
# print(lang_repos)

# 7 - Contando ocorrências das linguagens
print(Counter(lang_repos))

# 8 - Criando Dataframe

dados_obc = pd.DataFrame()
dados_obc['repo_name'] = name_repos
dados_obc['repo_lang'] = lang_repos
# print(dados_obc)

# 9 - Exportando para CSV
dados_obc.to_csv('obc.csv')
