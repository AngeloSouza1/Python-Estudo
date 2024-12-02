from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import time

def extract_total_results_with_selenium(term, geckodriver_path="/usr/local/bin/geckodriver", headless=True):
    """
    Usa Selenium com Firefox para carregar uma página e extrair o total de resultados.

    Args:
        term (str): Termo de pesquisa para a pesquisa no Google.
        geckodriver_path (str): Caminho para o executável do Geckodriver.
        headless (bool): Se True, executa o navegador em modo headless (sem interface gráfica).

    Returns:
        str: Texto contendo o total de resultados ou uma mensagem de erro.
    """
    try:
        # Construção da URL de pesquisa no Google
        url = f"https://www.google.com/search?q={term.replace(' ', '+')}"

        # Configuração do Firefox
        firefox_options = Options()
        if headless:
            firefox_options.add_argument("--headless")  # Executa em modo headless (sem interface gráfica)

        # Caminho para o geckodriver
        service = Service(geckodriver_path)

        # Inicializa o WebDriver do Firefox
        driver = webdriver.Firefox(service=service, options=firefox_options)

        # Abre a página
        driver.get(url)
        time.sleep(3)  # Aguarda a página carregar (ajuste conforme necessário)

        # Obtém o HTML da página
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')

        # Fecha o navegador
        driver.quit()

        # Busca pelo elemento que contém o número de resultados
        result_stats = soup.find("div", id="result-stats")  # Verificar o ID correto inspecionando a página

        if result_stats:
            return result_stats.text.strip()
        else:
            return "Não foi possível encontrar a totalização de resultados na página."
    except Exception as e:
        return f"Erro ao processar a página com Selenium: {e}"

       