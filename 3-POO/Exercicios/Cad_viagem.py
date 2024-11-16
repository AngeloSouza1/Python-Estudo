class Viagem:
    def __init__(self, destino):
        """
        Construtor para inicializar a viagem com um destino.
        
        Parâmetros:
        destino (str): Nome do destino da viagem.
        """
        self.destino = destino

    def __str__(self):
        """
        Retorna uma representação textual do destino da viagem.
        """
        return f"Destino: {self.destino}"


class CadastroViagem:
    def __init__(self, nome_usuario):
        """
        Construtor para inicializar o cadastro com o nome do usuário.
        
        Parâmetros:
        nome_usuario (str): Nome do usuário que está cadastrando a viagem.
        """
        self.nome_usuario = nome_usuario
        self.destino_selecionado = None

    def selecionar_destino(self, destinos):
        """
        Exibe uma lista de destinos disponíveis e permite ao usuário selecionar um.

        Parâmetros:
        destinos (list): Lista de instâncias da classe Viagem.
        """
        print(f"\nOlá, {self.nome_usuario}! Por favor, selecione seu destino:")
        for i, viagem in enumerate(destinos, start=1):
            print(f"{i}. {viagem.destino}")

        escolha = int(input("Digite o número do destino escolhido: "))
        if 1 <= escolha <= len(destinos):
            self.destino_selecionado = destinos[escolha - 1]
            print(f"\nCadastro realizado com sucesso!")
            print(f"{self.nome_usuario}, sua viagem para {self.destino_selecionado.destino} foi cadastrada.\n")
        else:
            print("Opção inválida! Por favor, selecione um número da lista de destinos.")


# Exemplo de uso
# Criando destinos disponíveis
destino1 = Viagem("Paris")
destino2 = Viagem("Nova York")
destino3 = Viagem("Tóquio")
destinos = [destino1, destino2, destino3]

# Solicitando o nome do usuário
nome_usuario = input("Digite seu nome para cadastrar uma viagem: ")
cadastro = CadastroViagem(nome_usuario)

# Permitindo que o usuário selecione um destino
cadastro.selecionar_destino(destinos)
