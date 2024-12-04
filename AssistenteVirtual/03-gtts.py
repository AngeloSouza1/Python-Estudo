from gtts import gTTS
import os

def falar_gtts(texto, arquivo="fala.mp3"):
    """Converte texto em fala usando gTTS e reproduz com comando do sistema."""
    try:
        # Gerar o arquivo de áudio
        tts = gTTS(texto, lang='pt-br')
        tts.save(arquivo)
        print(f"Áudio salvo como: {arquivo}")

        # Reproduzir o áudio
        os.system(f"mpg123 {arquivo}")  # Linux
    except Exception as e:
        print(f"Erro ao processar o texto: {e}")

# Testar o código
texto = "Olá! Eu sou sua assistente virtual e estou funcionando com comando de sistema!"
falar_gtts(texto)
