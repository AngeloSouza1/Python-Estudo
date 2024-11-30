from bs4 import BeautifulSoup

# 1 - Importando arquivo local
with open('pages/index.html', 'r') as file_html:
     content = file_html.read()
    #  print(content)
     soup = BeautifulSoup(content, 'lxml')
     print(soup.prettify())
     
# 2 - Recuperando títulos das vagas
     vagas = soup.find('h5')
     cursos = soup.find_all('h5')
    #  print(cursos)
     for curso in cursos:
         print(curso.text)