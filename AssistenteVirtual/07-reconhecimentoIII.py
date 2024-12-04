from random import randint
import speech_recognition as sr
from gtts import gTTS
import pygame
import time


def cria_audio(audio, mensagem):
    """
    Gera o áudio a partir de um texto e o reproduz usando pygame.
    :param audio: Nome do arquivo de áudio gerado.
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


# Criar e reproduzir o áudio inicial
cria_audio('wellcome.mp3', 'Escolha um número entre 1 a 10')

# Configurar o reconhecedor de fala
recon = sr.Recognizer()

try:
    with sr.Microphone() as source:
        print("Diga alguma coisa:")
        # Ajustar para ruído de fundo
        recon.adjust_for_ambient_noise(source, duration=1)

        # Capturar áudio com detecção automática de silêncio
        print("Gravando... Fale algo.")
        audio = recon.listen(source, timeout=None, phrase_time_limit=None)

        # Reconhecer a fala
        numero_texto = recon.recognize_google(audio, language="pt-BR")
        print(f"Você disse: {numero_texto}")

        # Mapeamento de palavras para números
        word_to_digit = {
            'um': 1,
            'dois': 2,
            'três': 3,
            'quatro': 4,
            'cinco': 5,
            'seis': 6,
            'sete': 7,
            'oito': 8,
            'nove': 9,
            'dez': 10
        }

        numero_digito = word_to_digit.get(numero_texto.lower())
        if numero_digito is None:
            cria_audio("invalido.mp3", "Número inválido. Por favor, tente novamente.")
        else:
            resultado = randint(1, 10)
            print(f"Número gerado: {resultado}")

            if numero_digito == resultado:
                cria_audio("venceu.mp3", "Parabéns. Você acertou o número!")
            else:
                cria_audio("perdeu.mp3", "Infelizmente você errou. Tente novamente.")

except sr.UnknownValueError:
    cria_audio("erro.mp3", "Não foi possível entender o que você disse.")
except sr.RequestError as e:
    cria_audio("erro_conexao.mp3", f"Erro ao se comunicar com o serviço de reconhecimento: {e}")
except Exception as e:
    print(f"Erro inesperado: {e}")
