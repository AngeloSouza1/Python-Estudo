import os
import sys
import time

# Função para limpar a tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para exibir texto em amarelo
def texto_amarelo(texto):
    amarelo = '\033[93m'
    reset = '\033[0m'
    print(f"{amarelo}{texto}{reset}")

# Função para pausar até que o usuário pressione uma tecla
def pausar():
    print("\nPressione qualquer tecla para continuar...")
    input()  # Aguarda qualquer entrada do usuário

# Função para calcular o preço da passagem
def calcular_distancia():
    limpar_tela()
    distancia = float(input("Digite a distância da viagem em km: "))
    if distancia <= 200:
        preco = distancia * 0.50
    else:
        preco = distancia * 0.35
    texto_amarelo(f"O preço da passagem é: R$ {preco:.2f}")
    pausar()

# Função para calcular o aumento do salário
def calcular_aumento_salario():
    limpar_tela()
    salario = float(input("Digite o salário do funcionário: R$ "))
    if salario > 1250:
        aumento = salario * 0.10  # 10% de aumento
    else:
        aumento = salario * 0.15  # 15% de aumento
    novo_salario = salario + aumento
    texto_amarelo(f"O novo salário do funcionário é: R$ {novo_salario:.2f}")
    pausar()

# Loop principal do menu
while True:
    limpar_tela()
    print("Menu de Opções:")
    print("1 - Calcular preço da passagem")
    print("2 - Calcular aumento de salário")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        calcular_distancia()
    elif opcao == "2":
        calcular_aumento_salario()
    elif opcao == "3":
        limpar_tela()
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida! Tente novamente.")
        time.sleep(2)  # Pausa para mostrar a mensagem antes de limpar a tela
