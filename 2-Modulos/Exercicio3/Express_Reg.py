import re
from colorama import Fore, Style, init

# Inicializa o colorama para suportar cores no terminal
init(autoreset=True)

def verificar_conteudo_string(texto):
    """
    Verifica se uma string contém apenas caracteres a-z, A-Z e 0-9.
    Se houver caracteres não permitidos, exibe-os em amarelo.
    
    Parâmetros:
    texto (str): A string a ser verificada.
    
    Retorna:
    bool: True se a string contém apenas os caracteres permitidos, False caso contrário.
    """
    # Expressão regular para verificar caracteres válidos
    if re.fullmatch(r'^[a-zA-Z0-9]+$', texto):
        return True
    else:
        # Identifica e exibe caracteres não permitidos em amarelo
        invalidos = [char for char in texto if not re.match(r'[a-zA-Z0-9]', char)]
        print("A string contém caracteres não permitidos:", end=" ")
        for char in invalidos:
            print(Fore.YELLOW + char + Style.RESET_ALL, end=" ")
        print()  # Nova linha após exibir caracteres inválidos
        return False

# Exemplo de uso
texto = input("Digite uma string: ")
if verificar_conteudo_string(texto):
    print("A string contém apenas caracteres permitidos (a-z, A-Z, 0-9).")
else:
    print("A string contém caracteres fora do conjunto permitido.")
