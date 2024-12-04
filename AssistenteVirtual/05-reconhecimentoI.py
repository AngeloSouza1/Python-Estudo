import speech_recognition as sr
import sounddevice as sd
import wave

def gravar_audio(duracao=10, taxa_amostragem=44100, nome_arquivo="gravacao.wav"):
    """
    Grava o áudio do microfone e salva como arquivo WAV (formato PCM).
    :param duracao: Duração da gravação em segundos.
    :param taxa_amostragem: Taxa de amostragem do áudio.
    :param nome_arquivo: Nome do arquivo de saída.
    """
    print(f"Gravando por {duracao} segundos...")
    audio = sd.rec(int(duracao * taxa_amostragem), samplerate=taxa_amostragem, channels=1, dtype='int16')
    sd.wait()  # Aguarda o término da gravação
    
    # Salvar o áudio no formato WAV (PCM)
    with wave.open(nome_arquivo, 'wb') as wf:
        wf.setnchannels(1)  # Canal mono
        wf.setsampwidth(2)  # 16 bits (int16)
        wf.setframerate(taxa_amostragem)  # Taxa de amostragem
        wf.writeframes(audio.tobytes())
    
    print(f"Áudio salvo como: {nome_arquivo}")
    return nome_arquivo

def reconhecer_audio(nome_arquivo):
    """
    Processa o arquivo de áudio e realiza o reconhecimento de fala.
    :param nome_arquivo: Caminho para o arquivo de áudio.
    """
    recon = sr.Recognizer()
    try:
        with sr.AudioFile(nome_arquivo) as source:
            print("Carregando o áudio para reconhecimento...")
            audio = recon.record(source)  # Lê todo o áudio do arquivo
            texto = recon.recognize_google(audio, language='pt-BR')
            print(f"Texto reconhecido: {texto}")
    except sr.UnknownValueError:
        print("Não foi possível entender o áudio.")
    except sr.RequestError as e:
        print(f"Erro ao se comunicar com o serviço de reconhecimento: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

# Gravar e reconhecer
arquivo_audio = gravar_audio(duracao=10)
reconhecer_audio(arquivo_audio)
