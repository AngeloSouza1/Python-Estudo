from requests import get
from bs4 import BeautifulSoup

def ultima_noticias():
    """
    Busca as 3 últimas notícias do feed RSS e retorna seus títulos concatenados.
    """
    url = 'https://news.google.com/rss?gl=BR&hl=pt-BR&ceid=BR:pt-419'
    site = get(url)
    noticias = BeautifulSoup(site.content, 'xml')
    
    titulos = []
    for item in noticias.findAll('item')[:3]:
        titulo = item.title.text.strip()  # Remover espaços em branco ao redor
        titulos.append(titulo)
    
    # Concatenar as notícias em uma única string
    return " Aqui estão as últimas notícias: " + " ".join(titulos)
