import os
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
import matplotlib.pyplot as plt

# Baixar o recurso 'punkt', se necessário
nltk.download('punkt')

# Caminho para o arquivo
file_path = os.path.join("data", "texto.txt")

# 1 - Importação do Texto
if os.path.exists(file_path):  # Verificar se o arquivo existe
    with open(file_path, "r", encoding="utf-8") as file:
        texto = file.read()
        print("Texto importado com sucesso!")
        # print(texto)
else:
    print(f"Erro: O arquivo '{file_path}' não foi encontrado.")
    exit()  # Sair do programa se o arquivo não existir

# 2 - Tokenizando o Texto
try:
    print("\n--- Tokenização em sentenças ---")
    sent_tokens = sent_tokenize(texto, language="portuguese")  
    print(sent_tokens)
    print(f"Número de sentenças: {len(sent_tokens)}")

    print("\n--- Tokenização em palavras ---")
    word_tokens = word_tokenize(texto, language="portuguese") 
    print(word_tokens)
    print(f"Número de palavras: {len(word_tokens)}")

except LookupError as e:
    print(f"Erro ao realizar a tokenização: {e}")
    print("Certifique-se de que os pacotes necessários do NLTK estão instalados.")

# 3 - Frequência de Distribuição
print("\n--- Frequência de Distribuição ---")
fdist = FreqDist(word_tokens)
print(fdist.most_common(10))

# Plotando o gráfico ou salvando como imagem
fdist.plot(10)
plt.savefig("frequencia_distribuicao.png")
print("Gráfico salvo como 'frequencia_distribuicao.png'")
