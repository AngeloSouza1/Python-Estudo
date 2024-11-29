import requests

# URL corrigida: remova os colchetes angulares (< e >)
link = 'https://www.google.com/search?q=cota%C3%A7%C3%A3o+dolar'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}

# Enviando a requisição GET
requisicao = requests.get(link, headers=headers)

# Imprimindo a resposta e o código de status
print(requisicao)
print(requisicao.status_code)

#  Opcional: descomente para imprimir o conteúdo da resposta
# print(requisicao.text)
