import os
import time
from colorama import Fore, Style, init

# Inicializa o colorama para suportar cores no terminal
init(autoreset=True)

def limpar_tela():
    # Limpa a tela do terminal
    os.system('cls' if os.name == 'nt' else 'clear')

def contagem_regressiva():
    limpar_tela()
    print("Iniciando contagem regressiva para o lançamento do foguete!\n")
    for i in range(10, -1, -1):
        print(Fore.YELLOW + str(i) + Style.RESET_ALL)
        time.sleep(1)
    print("Lançamento! 🚀\a")  # Exibe o "beep" após a contagem
    input("\nPressione Enter para voltar ao menu...")

def tabuada():
    limpar_tela()
    numero = int(input("Digite o número para calcular a tabuada: "))
    inicio = int(input("Digite o valor inicial do intervalo: "))
    fim = int(input("Digite o valor final do intervalo: "))
    
    print(f"\n{Fore.YELLOW}Tabuada do número {numero}, do {inicio} até {fim}:{Style.RESET_ALL}")
    for i in range(inicio, fim + 1):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
    
    input("\nPressione Enter para voltar ao menu...")

def menu():
    while True:
        limpar_tela()
        print("Escolha uma opção:")
        print("1 - Contagem Regressiva para Lançamento")
        print("2 - Calcular Tabuada de um Número")
        print("3 - Sair")

        opcao = input("Digite a opção desejada: ")
        
        if opcao == '1':
            contagem_regressiva()
        elif opcao == '2':
            tabuada()
        elif opcao == '3':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")
            input("\nPressione Enter para continuar...")

# Executa o menu principal
menu()
