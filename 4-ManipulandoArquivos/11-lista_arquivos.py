import glob
import os
import zipfile

# Exibe o diretório atual de trabalho
print("📂 Diretório atual de trabalho:", os.getcwd())

# Função para listar arquivos em uma extensão específica dentro da pasta "dados"
def listar_arquivos(pasta, extensao):
    arquivos = glob.glob(f"{pasta}/*.{extensao}")
    if arquivos:
        print(f"\n📄 Arquivos .{extensao} encontrados na pasta '{pasta}':")
        for file in arquivos:
            print("  -", os.path.basename(file))
    else:
        print(f"\n⚠️ Nenhum arquivo .{extensao} encontrado na pasta '{pasta}'.")
    return arquivos

# Função para compactar arquivos e salvar em um arquivo .zip
def compactar_arquivos(arquivos, destino_zip):
    if arquivos:
        with zipfile.ZipFile(destino_zip, 'w') as f:
            for file in arquivos:
                f.write(file)
        print(f"✅ Arquivos compactados em '{destino_zip}'")
    else:
        print(f"⚠️ Nenhum arquivo encontrado para compactação em '{destino_zip}'.")

# Verifica se a pasta "dados" existe
if not os.path.isdir('dados'):
    print("\n❌ A pasta 'dados' não existe no diretório atual. Certifique-se de que ela está presente e tente novamente.")
else:
    print("\n✅ A pasta 'dados' foi encontrada.\n")

    # 1 - Listando e compactando arquivos .txt
    txt_files = listar_arquivos("dados", "txt")
    compactar_arquivos(txt_files, 'dados/names.zip')

    # 2 - Listando e compactando arquivos .csv
    csv_files = listar_arquivos("dados", "csv")
    compactar_arquivos(csv_files, 'dados/languages.zip')

    # 3 - Compactando todos os arquivos da pasta "dados"
    all_files = glob.glob("dados/*")
    if all_files:
        print("\n📦 Compactando todos os arquivos da pasta 'dados' em 'dados/code.zip':")
        for file in all_files:
            print("  -", os.path.basename(file))
        compactar_arquivos(all_files, 'dados/code.zip')
    else:
        print("\n⚠️ Nenhum arquivo encontrado na pasta 'dados' para compactar.")
