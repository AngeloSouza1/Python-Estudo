# main.py

from agenda import Agenda
from colorama import Fore, Style, init

init(autoreset=True)

def exibir_menu():
    print(Fore.CYAN + "\n==============================")
    print("       AGENDA DE CONTATOS      ")
    print("==============================\n" + Style.RESET_ALL)
    print("1. Adicionar Contato")
    print("2. Listar Contatos")
    print("3. Remover Contato")
    print("4. Alterar Contato")
    print("5. Sair\n")

def adicionar_contato(agenda):
    print(Fore.YELLOW + "\n--- Adicionar Novo Contato ---" + Style.RESET_ALL)
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    email = input("Digite o email do contato: ")
    agenda.adicionar_contato(nome, telefone, email)

def listar_contatos(agenda):
    print(Fore.YELLOW + "\n--- Lista de Contatos ---" + Style.RESET_ALL)
    agenda.listar_contatos()
    input("\nPressione Enter para retornar ao menu principal...")

def remover_contato(agenda):
    print(Fore.YELLOW + "\n--- Remover Contato ---" + Style.RESET_ALL)
    nome = input("Digite o nome do contato a ser removido: ")
    agenda.remover_contato(nome)
    input("\nPressione Enter para retornar ao menu principal...")

def alterar_contato(agenda):
    print(Fore.YELLOW + "\n--- Alterar Contato ---" + Style.RESET_ALL)
    nome = input("Digite o nome do contato a ser alterado: ")
    agenda.alterar_contato(nome)
    input("\nPressione Enter para retornar ao menu principal...")

def main():
    agenda = Agenda()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_contato(agenda)
        elif opcao == '2':
            listar_contatos(agenda)
        elif opcao == '3':
            remover_contato(agenda)
        elif opcao == '4':
            alterar_contato(agenda)
        elif opcao == '5':
            print(Fore.GREEN + "Saindo da agenda de contatos. Até logo!" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Opção inválida. Por favor, escolha uma opção válida.\n" + Style.RESET_ALL)

if __name__ == "__main__":
    main()
