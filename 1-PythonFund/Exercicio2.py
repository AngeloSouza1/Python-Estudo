import os
from colorama import Fore, Style, init

# Inicializa o colorama para suportar cores no terminal
init(autoreset=True)

def limpar_tela():
    # Limpa a tela do terminal
    os.system('cls' if os.name == 'nt' else 'clear')

def substituir_caractere_repetido():
    limpar_tela()
    texto = input("Digite uma string: ")
    if texto:
        primeiro_caractere = texto[0]
        resultado = primeiro_caractere + texto[1:].replace(primeiro_caractere, '$')
        print(f"{Fore.YELLOW}Resultado: {resultado}{Style.RESET_ALL}")
    else:
        print("String vazia fornecida.")
    input("\nPressione Enter para voltar ao menu...")

def trocar_caracteres_iniciais():
    limpar_tela()
    str1 = input("Digite a primeira string: ")
    str2 = input("Digite a segunda string: ")
    
    if len(str1) >= 2 and len(str2) >= 2:
        nova_str1 = str2[:2] + str1[2:]
        nova_str2 = str1[:2] + str2[2:]
        resultado = nova_str1 + " " + nova_str2
        print(f"{Fore.YELLOW}Resultado: {resultado}{Style.RESET_ALL}")
    else:
        print("As duas strings devem ter pelo menos 2 caracteres.")
    
    input("\nPressione Enter para voltar ao menu...")

def menu():
    while True:
        limpar_tela()
        print("Escolha uma opção:")
        print("1 - Substituir caracteres repetidos em uma string")
        print("2 - Trocar os dois primeiros caracteres entre duas strings")
        print("3 - Sair")

        opcao = input("Digite a opção desejada: ")
        
        if opcao == '1':
            substituir_caractere_repetido()
        elif opcao == '2':
            trocar_caracteres_iniciais()
        elif opcao == '3':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")
            input("\nPressione Enter para continuar...")

# Executa o menu principal
menu()
