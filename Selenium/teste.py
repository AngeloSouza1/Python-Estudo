from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# 1 - Termo de pesquisa
term = input('Digite o que deseja pesquisar:\n')

# 2 - Iniciando o Driver
browser = webdriver.Firefox()
browser.get('https://www.google.com.br/')

# 3 - Encontrando o elemento
elem = browser.find_element(
    By.XPATH,
    "//textarea[@aria-label='Pesquisar']"
)

# 4 - Enviando termo para pesquisa
elem.send_keys(term)
elem.send_keys(Keys.ENTER)

# 5 - Retornando a Qtd de Registros
time.sleep(5)  # Tempo para garantir o carregamento da página

# Tentar encontrar o número de resultados
try:
    results = browser.find_element(By.ID, 'result-stats').text
    print(f'Foram encontrados {results}')
except Exception as e:
    print("Não foi possível encontrar o número de resultados na página.")
    results = None

# 6 - Salvar o HTML da página para depuração
html_content = browser.page_source
debug_file = 'debug_google_results.html'
try:
    with open(debug_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"Arquivo de depuração salvo como {debug_file}.")
except Exception as e:
    print(f"Erro ao salvar o arquivo de depuração: {e}")

# 7 - Fechar o navegador
browser.quit()

