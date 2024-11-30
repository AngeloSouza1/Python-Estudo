from bs4 import BeautifulSoup

# Importando arquivo local
with open('pages/index.html', 'r', encoding='utf-8') as file_html:
    content = file_html.read()

# Inicializando o BeautifulSoup
soup = BeautifulSoup(content, 'lxml')

# Recuperando os títulos dos cursos
cursos = soup.find_all('div', class_='card-header')

# Recuperando os preços dos cursos
precos = soup.find_all('a', class_='btn btn-block')

# Criando a lista com títulos e preços
if not cursos or not precos:
    print("Nenhum curso ou preço encontrado.")
else:
    cursos_e_precos = []
    for curso, preco in zip(cursos, precos):
        titulo = curso.text.strip()
        valor = preco.text.strip().replace("Inicie por ", "")
        cursos_e_precos.append({"curso": titulo, "preco": valor})

    # Imprimindo os resultados
    for item in cursos_e_precos:
        print(f"Curso: {item['curso']} - Preço: {item['preco']}")
