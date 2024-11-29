# 1 - Conhecendo a API
# <https://jsonplaceholder.typicode.com/posts>

# 2 - Lendo dados com Get
import requests

# The API endpoint
url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

print(response.status_code)

# Print the response pega os dados e converte para json
response_json = response.json()
print(response_json)


# Exemplo de tratamento

if response.status_code == 200:
    print("Requisição bem sucedida")
else:  
    print("Requisição mal sucedida")  # ou print(f"Requisição
    
    