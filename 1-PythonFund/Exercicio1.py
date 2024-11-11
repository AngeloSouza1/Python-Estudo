import os
from colorama import Fore, Style, init

# Inicializa o colorama para suportar cores no terminal
init(autoreset=True)

def limpar_tela():
    # Limpa a tela do terminal
    os.system('cls' if os.name == 'nt' else 'clear')

def antecessor_sucessor():
    limpar_tela()
    numero = int(input("Digite um número: "))
    antecessor = numero - 1
    sucessor = numero + 1
    print(f"{Fore.YELLOW}O antecessor de {numero} é {antecessor} e o sucessor é {sucessor}.{Style.RESET_ALL}")
    input("\nPressione Enter para voltar ao menu...")

def media_notas():
    limpar_tela()
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    nota4 = float(input("Digite a quarta nota: "))
    media = (nota1 + nota2 + nota3 + nota4) / 4
    print(f"{Fore.YELLOW}A média das quatro notas é: {media:.2f}{Style.RESET_ALL}")
    input("\nPressione Enter para voltar ao menu...")

def menu():
    while True:
        limpar_tela()
        print("Escolha uma opção:")
        print("1 - Calcular Antecessor e Sucessor de um número")
        print("2 - Calcular a Média de 4 Notas")
        print("3 - Sair")

        opcao = input("Digite a opção desejada: ")
        
        if opcao == '1':
            antecessor_sucessor()
        elif opcao == '2':
            media_notas()
        elif opcao == '3':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")
            input("\nPressione Enter para continuar...")

# Executa o menu principal
menu()
