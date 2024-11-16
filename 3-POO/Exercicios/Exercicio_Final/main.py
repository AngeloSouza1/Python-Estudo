# main.py
import os
from contact import Contact, ContactBook
from colorama import Fore, Style, init

# Inicializa o colorama para colorir o texto no terminal
init(autoreset=True)

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_menu():
    limpar_tela()
    print(Fore.CYAN + "\n==============================")
    print("       AGENDA DE CONTATOS      ")
    print("==============================\n" + Style.RESET_ALL)
    print("1. Adicionar Contato")
    print("2. Listar Contatos")
    print("3. Buscar Contato")
    print("4. Remover Contato")
    print("5. Sair\n")

def adicionar_contato(agenda):
    limpar_tela()
    print(Fore.YELLOW + "\n--- Adicionar Novo Contato ---" + Style.RESET_ALL)
    name = input("Digite o nome do contato: ")
    phone = input("Digite o telefone do contato: ")
    email = input("Digite o email do contato: ")
    novo_contato = Contact(name, phone, email)
    agenda.add_contact(novo_contato)
    input("\nPressione Enter para retornar ao menu principal...")

def listar_contatos(agenda):
    limpar_tela()
    print(Fore.YELLOW + "\n--- Lista de Contatos ---" + Style.RESET_ALL)
    agenda.list_contacts()
    input("\nPressione Enter para retornar ao menu principal...")

def buscar_contato(agenda):
    limpar_tela()
    print(Fore.YELLOW + "\n--- Buscar Contato ---" + Style.RESET_ALL)
    name = input("Digite o nome do contato para buscar: ")
    agenda.search_contact(name)
    input("\nPressione Enter para retornar ao menu principal...")

def remover_contato(agenda):
    limpar_tela()
    print(Fore.YELLOW + "\n--- Remover Contato ---" + Style.RESET_ALL)
    name = input("Digite o nome do contato para remover: ")
    agenda.remove_contact(name)
    input("\nPressione Enter para retornar ao menu principal...")

def main():
    agenda = ContactBook()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_contato(agenda)
        elif opcao == '2':
            listar_contatos(agenda)
        elif opcao == '3':
            buscar_contato(agenda)
        elif opcao == '4':
            remover_contato(agenda)
        elif opcao == '5':
            print(Fore.GREEN + "Saindo da agenda de contatos. Até logo!" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Opção inválida. Por favor, escolha uma opção válida.\n" + Style.RESET_ALL)

if __name__ == "__main__":
    main()
