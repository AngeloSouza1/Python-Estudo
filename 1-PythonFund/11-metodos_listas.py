gamesList = ["Fifa23", "Star Wars", "The Legend of Zelda", "Red Dead 2"]

# 1 - Tamanho da lista
print("1")
print(len(gamesList))

# 2 - Recupera um item da lista pelo índice
print("2")
print(gamesList.index("Star Wars"))

# 3 - Adiciona item ao final da lista

gamesList.append("Gta V")
print("3")
print(gamesList)

# 4 - Ordena lista
gamesList.sort()
#listaJogos.reverse()
print("4")
print(gamesList)

# 5 - Copia os itens de uma lista para outra
gamesReset = gamesList.copy()
gamesReset.remove('Fifa23')
gamesReset.remove('Star Wars')
print("5")
print("")
print(gamesReset)

# 6 - Remove todos os itens da lista
gamesList.clear()
print("6")
print(gamesList)