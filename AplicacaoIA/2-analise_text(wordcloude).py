import os
import nltk
from nltk import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageDraw

# Garantir que o recurso 'punkt' do NLTK esteja disponível
nltk.download('punkt')

# 1 - Importação do Texto
file_path = os.path.join("data", "texto.txt")
if os.path.exists(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        texto = file.read()
        print("Texto importado com sucesso!")
else:
    print(f"Erro: O arquivo '{file_path}' não foi encontrado.")
    exit()

# 2 - Tokenizando o Texto
sent_tokens = sent_tokenize(texto)
print(f"Número de sentenças: {len(sent_tokens)}")

word_tokens = word_tokenize(texto)
print(f"Número de palavras: {len(word_tokens)}")

# 3 - Frequência de Distribuição
fdist = FreqDist(word_tokens)
print("\nFrequência de Distribuição (10 mais comuns):")
print(fdist.most_common(10))

# Plotar e salvar o gráfico de frequência
plt.figure(figsize=(12, 6))
fdist.plot(10)
plt.savefig("data/frequencia_distribuicao.png")
print("Gráfico de frequência salvo como 'frequencia_distribuicao.png'")

# 4 - WordCloud / WordCloud Customizado
def plot_cloud(wordcloud):
    plt.figure(figsize=(12, 8))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()

# Verificar e criar a máscara personalizada
mask_path = os.path.join("data", "upvote.png")
if os.path.exists(mask_path):
    print("Carregando máscara personalizada.")
    mascara = np.array(Image.open(mask_path))
else:
    print("Máscara personalizada não encontrada. Criando máscara padrão.")
    # Criar uma máscara simples (círculo vermelho)
    img = Image.new("RGB", (300, 300), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.ellipse((50, 50, 250, 250), fill=(255, 0, 0))
    img.save("data/upvote.png")
    mascara = np.array(img)

# Gerar a WordCloud
wordcloud = WordCloud(
    width=3000,
    height=2000,
    random_state=1,
    background_color='blue',
    colormap='Pastel1',
    collocations=False,
    stopwords=STOPWORDS,
    mask=mascara
).generate(texto)

# Exibir a WordCloud
plot_cloud(wordcloud)
