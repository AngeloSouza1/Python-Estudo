import os
import shutil

def organizar_arquivos(diretorio):
    """
    Organiza arquivos de um diretório em pastas de acordo com suas extensões.
    Apenas cria pastas para extensões encontradas no diretório.

    Parâmetros:
    diretorio (str): Caminho do diretório a ser organizado.
    """
    # Dicionário de categorias e extensões
    categorias = {
        "Imagens": ["jpg", "jpeg", "png", "gif", "bmp", "tiff", "webp", "svg"],
        "Documentos": ["pdf", "doc", "docx", "txt", "rtf", "odt"],
        "Planilhas": ["xls", "xlsx", "csv"],
        "Apresentações": ["ppt", "pptx"],
        "Áudio": ["mp3", "wav", "aac", "flac", "ogg", "m4a"],
        "Vídeo": ["mp4", "avi", "mkv", "mov", "wmv", "flv"],
        "Arquivos Compactados": ["zip", "rar", "tar", "gz", "7z"],
        "Executáveis": ["exe", "msi", "bat", "sh"],
        "Código-Fonte": ["py", "java", "cpp", "c", "js", "html", "css", "php", "xml", "json"],
    }

    if not os.path.exists(diretorio):
        raise FileNotFoundError(f"O diretório '{diretorio}' não existe.")

    arquivos_organizados = 0

    # Iterar sobre os arquivos no diretório
    for arquivo in os.listdir(diretorio):
        caminho_arquivo = os.path.join(diretorio, arquivo)

        if os.path.isfile(caminho_arquivo):
            extensao = arquivo.split('.')[-1].lower()
            movido = False

            # Encontra a categoria do arquivo
            for categoria, extensoes in categorias.items():
                if extensao in extensoes:
                    mover_para_pasta(diretorio, arquivo, categoria)
                    movido = True
                    arquivos_organizados += 1
                    print(f"Movido: {arquivo} -> {categoria}")  # Log de movimentação
                    break

            if not movido:
                # Caso a extensão não corresponda a nenhuma categoria
                mover_para_pasta(diretorio, arquivo, "Outros")
                arquivos_organizados += 1
                print(f"Movido: {arquivo} -> Outros")  # Log para "Outros"

    print(f"Organização concluída: {arquivos_organizados} arquivo(s) movido(s).")

def mover_para_pasta(diretorio, arquivo, categoria):
    """
    Move um arquivo para a pasta da categoria especificada.

    Parâmetros:
    diretorio (str): Diretório principal.
    arquivo (str): Nome do arquivo.
    categoria (str): Nome da categoria/pasta.
    """
    pasta_destino = os.path.join(diretorio, categoria)
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)  # Cria a pasta se não existir
    origem = os.path.join(diretorio, arquivo)
    destino = os.path.join(pasta_destino, arquivo)
    shutil.move(origem, destino)
    print(f"Arquivo movido para: {destino}")  # Log do movimento
