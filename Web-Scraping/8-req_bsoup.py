from bs4 import BeautifulSoup
import requests

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

        # Link da vaga
        link = vaga['href'] if vaga.has_attr('href') else 'Link não encontrado'

        # Exibir informações formatadas
        print(f"Vaga {index}:")
        print(f"  Título : {titulo}")
        print(f"  Local  : {local}")
        print(f"  Link   : {link}")
        print("") 
        print("-" * 60)
        print("") 
