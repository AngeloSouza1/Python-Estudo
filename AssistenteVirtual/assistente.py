from gtts import gTTS
import pygame
import speech_recognition as sr
import sys
import time
import funcoes_so
import os
import funcoes_noticias
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
os.environ["SDL_AUDIODRIVER"] = "alsa"

def cria_audio(audio, mensagem):
    """
    Gera um áudio com gTTS e reproduz usando pygame.
    :param audio: Nome do arquivo de áudio.
    :param mensagem: Texto a ser convertido em fala.
    """
    tts = gTTS(mensagem, lang='pt-br')
    tts.save(audio)
    print(f"Áudio salvo como: {audio}")

    # Reproduzir o áudio usando pygame
    pygame.mixer.init()
    pygame.mixer.music.load(audio)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.3)  # Aguarda a reprodução terminar


def monitora_audio():
    """
    Monitora o microfone em busca de comandos de voz.
    :return: Texto reconhecido.
    """
    recon = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ajustando para o ruído de fundo...")
        recon.adjust_for_ambient_noise(source, duration=1)
        print("Diga alguma coisa...")
        audio = recon.listen(source)
        try:
            mensagem = recon.recognize_google(audio, language='pt-BR')
            mensagem = mensagem.lower()
            print("Você disse:", mensagem)
            executa_comandos(mensagem)
            return mensagem
        except sr.UnknownValueError:
            print("Não consegui entender o que você disse.")
        except sr.RequestError as e:
            print(f"Erro ao se comunicar com o serviço de reconhecimento: {e}")
        return None


    
def executa_comandos(acao):
    if 'fechar assistente' in acao:
        sys.exit()
    elif 'horas' in acao:
        cria_audio('mensagem.mp3',funcoes_so.verifica_hora())
    elif 'desligar computador' in acao and 'uma hora' in acao:
        funcoes_so.desliga_computador_uma_hora()
    elif 'desligar computador' in acao and 'meia hora' in acao:
        funcoes_so.desliga_computador_meia_hora()
    elif 'cancelar desligamento' in acao:
        funcoes_so.cancela_desligamento()
    elif 'notícias' in acao:
        cria_audio('mensagem.mp3', funcoes_noticias.ultima_noticias())


def main():
    """
    Função principal do assistente virtual.
    """
    cria_audio("wellcome.mp3", "Olá, sou a Maria. Em que posso lhe ajudar?")
    while True:
        monitora_audio()


if __name__ == "__main__":
    main()
