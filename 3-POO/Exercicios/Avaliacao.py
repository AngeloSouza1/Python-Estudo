class Filme:
    def __init__(self, titulo):
        self.titulo = titulo
        self.avaliacoes = 0  # Soma total das avaliações
        self.total_avaliadores = 0  # Contador de avaliadores

    def avaliar(self, nota):
        """
        Adiciona uma avaliação ao filme, somando a nota e incrementando o contador de avaliadores.
        
        Parâmetros:
        nota (float): Nota dada ao filme.
        """
        if nota < 0 or nota > 10:
            print("Nota inválida! Insira uma nota entre 0 e 10.")
            return
        
        self.avaliacoes += nota
        self.total_avaliadores += 1
        print(f"Avaliação de {nota} adicionada para o filme '{self.titulo}'.")

    def media_avaliacao(self):
        """
        Calcula e retorna a média de avaliação do filme.
        
        Retorna:
        float: Média das avaliações ou 0 se não houver avaliadores.
        """
        if self.total_avaliadores == 0:
            return 0
        return self.avaliacoes / self.total_avaliadores

    def __str__(self):
        """
        Retorna uma representação textual do filme com sua média de avaliação.
        """
        return f"Filme: {self.titulo}, Média de Avaliação: {self.media_avaliacao():.2f} ({self.total_avaliadores} avaliadores)"



# Criação de um filme
filme1 = Filme("Inception")

# Avaliando o filme
filme1.avaliar(8)
filme1.avaliar(9.5)
filme1.avaliar(7)

# Exibindo informações do filme
print(filme1)  # Deve mostrar: Filme: Inception, Média de Avaliação: X.XX (3 avaliadores)
