from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time
from selenium_results_extractor import extract_total_results_with_selenium

# 1 - Termo de pesquisa
term = input('Digite o que deseja pesquisar:\n')

# Configurando o User-Agent no Firefox
options = Options()
options.set_preference(
    "general.useragent.override", 
    "Mozilla/5.0 (X11; Linux x86_64; rv:115.0) Gecko/20100101 Firefox/115.0"
)

# 2 - Iniciando o Driver com o User-Agent configurado
browser = None  # Inicializamos o navegador como None para garantir o fechamento
try:
    browser = webdriver.Firefox(options=options)
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

    # 7 - Navegando entre páginas
    url_page = browser.find_element(
        By.XPATH,
        '//a[@aria-label="Page 2"]').get_attribute('href')

    current_page = 0
    start = 10
    list_results = []

    while current_page <= 10:
        if not current_page == 0:
            url_page = url_page.replace(
                "start=%s" % start,
                "start=%s" % (start + 10),
            )
            start += 10
        current_page += 1
        browser.get(url_page)
        
    # 8 - Recuperando informações
        divs = browser.find_elements(
            By.XPATH,
            '//div[@class="yuRUbf"]'
        )
        for div in divs:
            name = div.find_element(By.TAG_NAME, 'h3')
            link = div.find_element(By.TAG_NAME, 'a')
            result = "%s,%s" %(name.text, link.get_attribute('href'))
            print(result)
            list_results.append(result)    
        

finally:
    # Garante o fechamento do navegador
    if browser:
        browser.quit()
