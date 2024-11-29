import requests

r = requests.get('https://api.github.com/events')

print(r)

print(r.status_code)

print(r.url)

print(r.text)

print(r.json())

r = requests.get('https://api.github.com/versions')

#Especificando versão
# headers = {'X-GitHub-Api-Version': '2022-11-28'}
# r = requests.get('<https://api.github.com/events>', headers=headers)

print(r.json())