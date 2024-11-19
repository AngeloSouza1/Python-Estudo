# agenda.py

import os

class Agenda:
    def __init__(self, arquivo='contatos.txt'):
        self.arquivo = arquivo

    def adicionar_contato(self, nome, telefone, email):
        with open(self.arquivo, 'a') as file:
            file.write(f"{nome},{telefone},{email}\n")
        print(f"Contato '{nome}' adicionado com sucesso!")

    def listar_contatos(self):
        if not os.path.exists(self.arquivo):
            print("Nenhum contato encontrado.")
            return

        with open(self.arquivo, 'r') as file:
            contatos = file.readlines()
            if not contatos:
                print("Nenhum contato encontrado.")
            else:
                print("\nLista de Contatos:")
                for linha in contatos:
                    nome, telefone, email = linha.strip().split(',')
                    print(f"Nome: {nome}, Telefone: {telefone}, Email: {email}")

    def remover_contato(self, nome):
        if not os.path.exists(self.arquivo):
            print("Nenhum contato encontrado para remover.")
            return

        with open(self.arquivo, 'r') as file:
            contatos = file.readlines()

        contatos_restantes = [linha for linha in contatos if not linha.startswith(nome + ',')]

        if len(contatos) == len(contatos_restantes):
            print(f"Contato '{nome}' não encontrado.")
        else:
            with open(self.arquivo, 'w') as file:
                file.writelines(contatos_restantes)
            print(f"Contato '{nome}' removido com sucesso!")

    def alterar_contato(self, nome):
        """
        Altera as informações de um contato existente.

        Parâmetros:
        nome (str): Nome do contato a ser alterado.
        """
        if not os.path.exists(self.arquivo):
            print("Nenhum contato encontrado para alterar.")
            return

        with open(self.arquivo, 'r') as file:
            contatos = file.readlines()

        contatos_alterados = []
        contato_encontrado = False

        for linha in contatos:
            dados = linha.strip().split(',')
            if dados[0].lower() == nome.lower():
                contato_encontrado = True
                print(f"\nContato encontrado: Nome: {dados[0]}, Telefone: {dados[1]}, Email: {dados[2]}")
                novo_nome = input("Digite o novo nome (ou pressione Enter para manter o atual): ") or dados[0]
                novo_telefone = input("Digite o novo telefone (ou pressione Enter para manter o atual): ") or dados[1]
                novo_email = input("Digite o novo email (ou pressione Enter para manter o atual): ") or dados[2]
                contatos_alterados.append(f"{novo_nome},{novo_telefone},{novo_email}\n")
                print(f"Contato '{nome}' alterado com sucesso!")
            else:
                contatos_alterados.append(linha)

        if contato_encontrado:
            with open(self.arquivo, 'w') as file:
                file.writelines(contatos_alterados)
        else:
            print(f"Contato '{nome}' não encontrado para alteração.")
