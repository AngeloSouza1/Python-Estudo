from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium_results_extractor import extract_total_results_with_selenium

# 1 - Termo de pesquisa
term = input('Digite o que deseja pesquisar:\n')

# 2 - Iniciando o Driver
browser = None  # Inicializamos o navegador como None para garantir o fechamento
try:
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
    time.sleep(2)

    # Chamada da função para extrair resultados
    result = extract_total_results_with_selenium(
        term,
        geckodriver_path="/usr/local/bin/geckodriver",  # Ajuste o caminho para o Geckodriver, se necessário
        headless=False  # Defina como True para executar em modo headless
    )
    # Exibe os resultados
    print(f"Foram encontrados: {result}")
    
    # 6 - Retornando o Número de Páginas
    qtd_results = int(result.split('Aproximadamente ')[1].split(' resultados')[0].replace('.', ''))
    tot_pages = qtd_results / 10

    # Melhorando a formatação do print
    print(f"Total de páginas estimadas: {tot_pages:,.0f}".replace(",", "."))


finally:
    # Garante o fechamento do navegador
    if browser:
        browser.quit()
