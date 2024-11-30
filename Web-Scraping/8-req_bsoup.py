from bs4 import BeautifulSoup
import requests
import pandas as pd

# URL da página
url = 'https://99jobs.com/opportunities/filtered_search?utf8=%E2%9C%93&search%5Bterm%5D=python'

# Fazer a requisição com cabeçalho para simular um navegador
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
response = requests.get(url, headers=headers)

# Parse do conteúdo HTML
soup = BeautifulSoup(response.text, 'lxml')

# Capturar as vagas
vagas = soup.find_all('a', class_='opportunity-card')

# Lista para armazenar os dados das vagas
dados_vagas = []

# Verificar se encontrou vagas
if not vagas:
    print("Nenhuma vaga encontrada.")
else:
    print(f"{len(vagas)} vagas encontradas:")
    print("=" * 60)

    # Iterar sobre as vagas e extrair informações
    for index, vaga in enumerate(vagas, start=1):
        # Título da vaga
        titulo = vaga.find('h1').text.strip() if vaga.find('h1') else 'Título não encontrado'

        # Local da vaga
        local = vaga.find('p').text.strip() if vaga.find('p') else 'Local não encontrado'

        # Nível da vaga
        nivel = vaga.find('span', class_='opportunity-label-level')
        nivel = nivel.text.strip() if nivel else 'Nível não informado'

        # Modelo de trabalho
        modelo = vaga.find('span', class_='opportunity-label-acting-mode')
        modelo = modelo.text.strip() if modelo else 'Modelo não informado'

        # Link da vaga
        link = vaga['href'] if vaga.has_attr('href') else 'Link não encontrado'

        # Exibir informações formatadas no terminal
        print(f"Vaga {index}:")
        print(f"  Título : {titulo}")
        print(f"  Local  : {local}")
        print(f"  Nível  : {nivel}")
        print(f"  Modelo : {modelo}")
        print(f"  Link   : {link}")
        print("-" * 60)

        # Adicionar informações em um dicionário
        dados_vagas.append({
            'Título da Vaga': titulo,
            'Local': local,
            'Nível': nivel,
            'Modelo de Trabalho': modelo,
            'Link da Vaga': link
        })

    # Criar um DataFrame a partir dos dados coletados
    df = pd.DataFrame(dados_vagas)

    # Formatar melhor o DataFrame para exportação
    df['Título da Vaga'] = df['Título da Vaga'].str.title()
    df['Local'] = df['Local'].str.title()
    df['Nível'] = df['Nível'].str.capitalize()
    df['Modelo de Trabalho'] = df['Modelo de Trabalho'].str.capitalize()

    # Salvar o DataFrame em um arquivo CSV
    df.to_csv('vagas_python_detalhadas.csv', index=False, encoding='utf-8', sep=';')

    print("\nDados exportados para 'vagas_python_detalhadas.csv'.")
