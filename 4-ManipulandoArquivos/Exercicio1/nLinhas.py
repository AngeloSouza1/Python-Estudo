import os
from colorama import Fore, Style, init

# Inicializa o colorama para colorir o texto no terminal
init(autoreset=True)

def ler_linhas(caminho_pasta, nome_arquivo, n):
    """
    Lê as primeiras n linhas de um arquivo em uma pasta específica.

    Parâmetros:
    caminho_pasta (str): O caminho da pasta onde o arquivo está localizado.
    nome_arquivo (str): O nome do arquivo dentro da pasta.
    n (int): O número de linhas a serem lidas.

    Retorna:
    list: Uma lista com as primeiras n linhas do arquivo.
    """
    caminho_completo = os.path.join(caminho_pasta, nome_arquivo)
    
    try:
        with open(caminho_completo, 'r') as arquivo:
            linhas = [arquivo.readline().strip() for _ in range(n)]
        return linhas
    except FileNotFoundError:
        print(Fore.RED + "Erro: O arquivo não foi encontrado no caminho especificado." + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Erro: {e}" + Style.RESET_ALL)

def main():
    print(Fore.CYAN + "\n==============================")
    print("     LEITOR DE ARQUIVO        ")
    print("==============================\n" + Style.RESET_ALL)
    
    caminho_pasta = input(Fore.YELLOW + "Digite o caminho da pasta onde o arquivo está localizado: " + Style.RESET_ALL)
    nome_arquivo = input(Fore.YELLOW + "Digite o nome do arquivo: " + Style.RESET_ALL)
    
    try:
        n = int(input(Fore.YELLOW + "Digite o número de linhas que deseja ler: " + Style.RESET_ALL))
    except ValueError:
        print(Fore.RED + "Erro: Por favor, insira um número válido para a quantidade de linhas." + Style.RESET_ALL)
        return

    linhas_lidas = ler_linhas(caminho_pasta, nome_arquivo, n)

    if linhas_lidas:
        print(Fore.GREEN + "\nAs primeiras linhas do arquivo são:\n" + Style.RESET_ALL)
        for linha in linhas_lidas:
            print(Fore.CYAN + linha + Style.RESET_ALL)

if __name__ == "__main__":
    main()
