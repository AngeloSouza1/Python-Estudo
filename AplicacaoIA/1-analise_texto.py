import os

# 1 - Importação do Texto
with open(os.path.join("data", "texto.txt"), "r", encoding="utf-8") as file:
    texto = file.read()
    print(texto)
    
# 2 - Tokenizando o Texto
sent_tokens = sent_tokenize(texto)
print(sent_tokens)
print(len(sent_tokens))

word_tokens = word_tokenize(texto)
print(word_tokens)
print(len(word_tokens))