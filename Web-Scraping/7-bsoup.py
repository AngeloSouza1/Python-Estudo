from bs4 import BeautifulSoup

# Importando arquivo local
with open('pages/index.html', 'r', encoding='utf-8') as file_html:
    content = file_html.read()

# Inicializando o BeautifulSoup
soup = BeautifulSoup(content, 'lxml')

# Recuperando os títulos dos cursos usando a classe 'card-header'
cursos = soup.find_all('div', class_='card-header')

# Verificando se encontrou elementos
if not cursos:
    print("Nenhum curso encontrado.")
else:
    # Iterando e imprimindo o texto de cada curso
    for curso in cursos:
        print(curso.text.strip())
