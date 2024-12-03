from goose3 import Goose
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import numpy as np

# nltk.download('stopwords')

# 1 - Importando Artigo da Internet
g = Goose()
# url = '<https://blog.geekhunter.com.br/pretensao-salarial-disparidade-generos/>'
url = 'https://olhardigital.com.br/2023/08/08/seguranca/google-chrome-vai-atualizar-sistema-mais-vezes-para-evitar-brechas-de-seguranca/'
artigo = g.extract(url)



# Melhorando a exibição dos dados
print("="*50)
print("Título do Artigo:")
print(artigo.title or "Título não encontrado")
print("="*50)

print("Descrição Meta:")
print(artigo.meta_description or "Descrição meta não encontrada")
print("="*50)

print("Data de Publicação:")
print(artigo.publish_date or "Data de publicação não encontrada")
print("="*50)

print("Texto Limpo do Artigo:")
print(artigo.cleaned_text or "Texto não encontrado")
print("="*50)

print("Links Encontrados no Artigo:")
if artigo.links:
    for idx, link in enumerate(artigo.links, start=1):
        print(f"[{idx}] {link}")
else:
    print("Nenhum link encontrado.")
print("="*50)


# 2 - Aplicando Análise Textual I
word_tokens = word_tokenize(artigo.cleaned_text)
print(word_tokens)
print(len(word_tokens))

portuguese_stops = set(stopwords.words('portuguese'))

# for palavra in word_tokens:
#     if palavra.lower() not in portuguese_stops:
#         print(palavra)
#         print(len(palavra))
palavras = [palavra for palavra in word_tokens if palavra.lower() not in portuguese_stops]
print(palavras)
print(len(palavras))