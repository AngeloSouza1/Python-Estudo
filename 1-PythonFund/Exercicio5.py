import os
from colorama import Fore, Style, init

# Inicializa o colorama para suportar cores no terminal
init(autoreset=True)

def limpar_tela():
    # Limpa a tela do terminal
    os.system('cls' if os.name == 'nt' else 'clear')

def contar_maiusculas_minusculas():
    limpar_tela()
    texto = input("Digite uma string: ")
    maiusculas = sum(1 for c in texto if c.isupper())
    minusculas = sum(1 for c in texto if c.islower())
    print(f"{Fore.YELLOW}Total de letras maiúsculas: {maiusculas}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Total de letras minúsculas: {minusculas}{Style.RESET_ALL}")
    input("\nPressione Enter para voltar ao menu...")

def separar_pares_impares():
    limpar_tela()
    numeros = input("Digite uma lista de números separados por espaço: ")
    lista_numeros = [int(n) for n in numeros.split()]
    pares = [num for num in lista_numeros if num % 2 == 0]
    impares = [num for num in lista_numeros if num % 2 != 0]
    
    print(f"{Fore.YELLOW}Números pares: {pares}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Números ímpares: {impares}{Style.RESET_ALL}")
    input("\nPressione Enter para voltar ao menu...")

def menu():
    while True:
        limpar_tela()
        print("Escolha uma opção:")
        print("1 - Contar letras maiúsculas e minúsculas em uma string")
        print("2 - Separar números pares e ímpares de uma lista")
        print("3 - Sair")

        opcao = input("Digite a opção desejada: ")
        
        if opcao == '1':
            contar_maiusculas_minusculas()
        elif opcao == '2':
            separar_pares_impares()
        elif opcao == '3':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")
            input("\nPressione Enter para continuar...")

# Executa o menu principal
menu()
