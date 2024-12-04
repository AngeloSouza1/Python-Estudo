from gtts import gTTS
import pygame
import time

def cria_audio(texto, arquivo="mensagem.mp3"):
    """Converte texto em fala e reproduz áudio com pygame."""
    try:
        tts = gTTS(texto, lang='pt-br')
        tts.save(arquivo)
        print(f"Áudio salvo como: {arquivo}")

        pygame.mixer.init()
        pygame.mixer.music.load(arquivo)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
    except Exception as e:
        print(f"Erro ao criar ou reproduzir o áudio: {e}")

Exemplo de uso
try:
    with open("dados/texto.txt", "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
        cria_audio(conteudo)
except FileNotFoundError:
    print("Erro: Arquivo 'dados/texto.txt' não encontrado.")
# cria_audio("testando")