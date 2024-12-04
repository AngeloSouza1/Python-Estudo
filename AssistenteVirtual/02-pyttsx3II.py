from gtts import gTTS
import os

def falar_gtts(texto, arquivo="fala.mp3", velocidade=1.25):
    """
    Converte texto em fala usando gTTS, ajusta a velocidade e reproduz o áudio.
    :param texto: Texto a ser falado.
    :param arquivo: Nome do arquivo de áudio gerado.
    :param velocidade: Fator de velocidade (ex: 1.0 normal, 1.25 rápido).
    """
    try:
        # Gerar o arquivo de áudio
        tts = gTTS(texto, lang='pt-br')
        tts.save(arquivo)
        print(f"Áudio salvo como: {arquivo}")

        # Ajustar a velocidade com sox
        ajustado = "fala_ajustada.mp3"
        os.system(f"sox {arquivo} {ajustado} tempo {velocidade}")
        print(f"Áudio ajustado salvo como: {ajustado}")

        # Reproduzir o áudio ajustado
        os.system(f"mpg123 {ajustado}")
    except Exception as e:
        print(f"Erro ao processar o texto: {e}")

# 1 - Utilizando o Input
# frase = input("Digite a frase a ser falada:\n")
# falar_gtts(frase, velocidade=1.5)

# 2 - Utilizando Leitura do Arquivo de Texto
try:
    with open("dados/texto.txt", "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
        falar_gtts(conteudo, velocidade=1.25)  # Velocidade mais rápida
except FileNotFoundError:
    print("Erro: Arquivo 'dados/texto.txt' não encontrado.")
