# contact.py

class Contact:
    def __init__(self, name, phone, email):
        """
        Construtor para inicializar um contato com nome, telefone e email.
        
        Parâmetros:
        name (str): Nome do contato.
        phone (str): Telefone do contato.
        email (str): Email do contato.
        """
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        """
        Retorna uma representação textual do contato.
        """
        return f"Nome: {self.name}, Telefone: {self.phone}, Email: {self.email}"


class ContactBook:
    def __init__(self):
        """
        Construtor para inicializar o livro de contatos como uma lista vazia.
        """
        self.contacts = []

    def add_contact(self, contact):
        """
        Adiciona um novo contato ao livro de contatos.
        
        Parâmetros:
        contact (Contact): Objeto do contato a ser adicionado.
        """
        self.contacts.append(contact)
        print(f"\nContato '{contact.name}' adicionado com sucesso!")

    def list_contacts(self):
        """
        Lista todos os contatos no livro de contatos.
        """
        if not self.contacts:
            print("\nA agenda de contatos está vazia.")
        else:
            print("\nLista de Contatos:")
            for contact in self.contacts:
                print(contact)

    def search_contact(self, name):
        """
        Busca um contato pelo nome.
        
        Parâmetros:
        name (str): Nome do contato a ser buscado.
        
        Retorna:
        Contact: O contato correspondente ou None se não encontrado.
        """
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print("\nContato encontrado:")
                print(contact)
                return contact
        print("\nContato não encontrado.")
        return None

    def remove_contact(self, name):
        """
        Remove um contato pelo nome.
        
        Parâmetros:
        name (str): Nome do contato a ser removido.
        """
        contact = self.search_contact(name)
        if contact:
            self.contacts.remove(contact)
            print(f"\nContato '{name}' removido com sucesso!")
        else:
            print("\nContato não encontrado para remoção.")
