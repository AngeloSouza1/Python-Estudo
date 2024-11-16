class Produto:
    def __init__(self, nome, preco):
        """
        Construtor para inicializar o produto com nome e preço.

        Parâmetros:
        nome (str): Nome do produto.
        preco (float): Preço original do produto.
        """
        self.nome = nome
        self.preco = preco

    def calcular_desconto(self, percentual):
        """
        Calcula o preço final com desconto.

        Parâmetros:
        percentual (float): Percentual de desconto a ser aplicado (entre 0 e 100).

        Retorna:
        float: Preço do produto após aplicar o desconto.
        """
        if percentual < 0 or percentual > 100:
            print("Percentual de desconto inválido! Insira um valor entre 0 e 100.")
            return self.preco

        desconto = self.preco * (percentual / 100)
        preco_final = self.preco - desconto
        return preco_final

    def __str__(self):
        """
        Retorna uma representação textual do produto com nome e preço.
        """
        return f"Produto: {self.nome}, Preço: R$ {self.preco:.2f}"


# Criação de um produto
produto1 = Produto("Notebook", 3000.00)

# Exibindo informações do produto
print(produto1)  # Exibe: Produto: Notebook, Preço: R$ 3000.00

# Calculando o preço com desconto
desconto = 15  # Percentual de desconto
preco_com_desconto = produto1.calcular_desconto(desconto)
print(f"Preço com {desconto}% de desconto: R$ {preco_com_desconto:.2f}")
