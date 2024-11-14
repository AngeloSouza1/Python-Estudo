import os

# 1. Exibir a pasta atual (diretório de trabalho)
print("Passo 1: Exibir o diretório de trabalho atual")
current_directory = os.getcwd()
print("Diretório atual:", current_directory)
print("-" * 40)  # Linha separadora para melhor visualização

# 2. Listar arquivos e pastas na pasta atual
print("Passo 2: Listar todos os arquivos e pastas no diretório atual")
directory_contents = os.listdir()
print("Conteúdo do diretório:")
for item in directory_contents:
    print(" -", item)
print("-" * 40)

# 3. Mostrar a versão do sistema operacional
print("Passo 3: Exibir a versão do sistema operacional")
# Em Linux, usamos 'uname -a' para obter informações do sistema
os.system('uname -a')
print("-" * 40)

# 4. Exibir informações sobre a máquina
print("Passo 4: Exibir informações da máquina")
# 'lscpu' fornece detalhes sobre a CPU
os.system('lscpu')
# 'cat /etc/os-release' mostra detalhes sobre o sistema operacional
os.system('cat /etc/os-release')
print("-" * 40)

# 5. Limpar a tela
print("Passo 5: Limpar a tela do terminal")
# 'clear' é o comando usado no Linux para limpar a tela
os.system('cls')
