import speech_recognition as sr
from gtts import gTTS
import pygame
import time
import sounddevice as sd
import wave


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


def gravar_audio(nome_arquivo="gravacao.wav", duracao=10, taxa_amostragem=44100):
    """
    Grava o áudio do microfone e salva como arquivo WAV.
    :param nome_arquivo: Nome do arquivo de saída.
    :param duracao: Duração da gravação em segundos.
    :param taxa_amostragem: Taxa de amostragem do áudio.
    """
    print(f"Gravando por {duracao} segundos...")
    audio = sd.rec(int(duracao * taxa_amostragem), samplerate=taxa_amostragem, channels=1, dtype='int16')
    sd.wait()  # Aguarda o término da gravação

    # Salvar o áudio no formato WAV
    with wave.open(nome_arquivo, 'wb') as wf:
        wf.setnchannels(1)  # Canal mono
        wf.setsampwidth(2)  # 16 bits (int16)
        wf.setframerate(taxa_amostragem)
        wf.writeframes(audio.tobytes())
    print(f"Áudio salvo como: {nome_arquivo}")
    return nome_arquivo


# Criar e reproduzir o áudio inicial
cria_audio('wellcome.mp3', 'Olá. Vou reconhecer a sua voz')

# Gravar áudio
arquivo_audio = gravar_audio(duracao=10)

# Configurar o reconhecedor de fala
recon = sr.Recognizer()

try:
    with sr.AudioFile(arquivo_audio) as source:
        print("Carregando o áudio gravado...")
        audio = recon.record(source)  # Processar o áudio gravado

        # Reconhecer a fala
        frase = recon.recognize_google(audio, language='pt-BR')
        print(f"Você disse: {frase}")
        cria_audio('mensagem.mp3', frase)
except sr.UnknownValueError:
    print("Não foi possível entender o áudio.")
except sr.RequestError as e:
    print(f"Erro ao se comunicar com o serviço de reconhecimento: {e}")
except Exception as e:
    print(f"Erro inesperado: {e}")
