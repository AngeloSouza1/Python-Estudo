
import sqlite3

# 1 - Conectando no BD
connection = sqlite3.connect("movies.db")

# 2 - Criando um cursor
'''
Cursor é um interador que permite
navegar e manipular os do bd.
'''
cursor = connection.cursor()

# 3 - Solicitando Dados do Usuário
name = input("Nome do Filme\\n")
year = int(input("Ano de lançamento\\n"))
score = float(input("Nota do filme\\n"))

# 3 - Inserindo Dados
cursor.execute("""
INSERT INTO movies (name, year, score)
VALUES (?,?,?)
""", (name, year, score))
connection.commit()
print('Dados inseridos com sucesso.')

# 5 - Fechando conexão
connection.close()
