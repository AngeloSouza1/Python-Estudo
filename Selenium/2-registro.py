from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time

# Configuração do GeckoDriver
firefox_service = Service('/usr/local/bin/geckodriver')  # Caminho do GeckoDriver
firefox_options = Options()
# firefox_options.add_argument('--headless')  # Executa em modo headless (opcional)

# Iniciando o navegador com as configurações
browser = webdriver.Firefox(service=firefox_service, options=firefox_options)

try:
    # 1 - Acessando o site
    browser.get('https://registro.br')

    # 2 - Buscando elementos
    elem = browser.find_element(By.ID, 'is-avail-field')
    elem.clear()
    elem.send_keys('botscompython.com.br')
    elem.send_keys(Keys.ENTER)
    
    time.sleep(5)  # Aguarda o carregamento dos resultados
    
    # Salvando captura de tela
    browser.save_screenshot('files/dominio.png')


    # 3 - Buscando informações
    results = browser.find_elements(By.TAG_NAME, 'strong')
    # import pdb
    # pdb.set_trace()
    print(f'Domínio {results[1].text} está {results[2].text}')



finally:
    # Encerra o navegador
    browser.quit()
