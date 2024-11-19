# name = input("Qual seu nome?\\n")

# r - leitura
# w - escrita
# a - append

# alternativa 1
#file = open("names.txt", "a")
#file.write(f"{name}\n")
#file.close()

# alternativa 2 mais usada
name = input("Qual seu nome?\n")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")