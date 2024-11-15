import random
from colorama import Fore, Style, init

# Inicializa o colorama para suportar cores no terminal
init(autoreset=True)

def jogo_adivinhacao():
    numero_aleatorio = random.randint(1, 10)  # Gera um número aleatório entre 1 e 10
    print(Fore.CYAN + "\n==============================")
    print("      JOGO DE ADIVINHAÇÃO      ")
    print("==============================\n" + Style.RESET_ALL)
    print("Tente adivinhar o número que estou pensando entre 1 e 10.")
    print(Fore.YELLOW + "Dica: Digite '0' para sair do jogo a qualquer momento.\n" + Style.RESET_ALL)

    while True:
        try:
            palpite = int(input(Fore.CYAN + "Digite seu palpite: " + Style.RESET_ALL))
            
            if palpite == 0:
                print(Fore.MAGENTA + "\nVocê escolheu sair do jogo. Até a próxima!\n" + Style.RESET_ALL)
                break

            if palpite < 1 or palpite > 10:
                print(Fore.RED + "Por favor, digite um número entre 1 e 10 ou '0' para sair." + Style.RESET_ALL)
                continue

            if palpite == numero_aleatorio:
                print(Fore.GREEN + "\nParabéns! Você acertou o número!\n" + Style.RESET_ALL)
                break
            elif palpite < numero_aleatorio:
                print(Fore.YELLOW + "Tente um número maior." + Style.RESET_ALL)
            else:
                print(Fore.YELLOW + "Tente um número menor." + Style.RESET_ALL)
                
        except ValueError:
            print(Fore.RED + "Entrada inválida. Por favor, digite um número válido." + Style.RESET_ALL)

# Inicia o jogo
jogo_adivinhacao()
