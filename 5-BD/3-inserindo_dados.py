import sqlite3

# 1 - Conectando no BD
connection = sqlite3.connect("movies.db")

# 2 - Criando um cursor
'''
Cursor é um interador que permite
navegar e manipular os do bd.
'''
cursor = connection.cursor()

# 3 - Inserindo Dados
cursor.execute("""
INSERT INTO movies (name, year, score)
VALUES ('Super Mario Bros', 2023, 9.5)
""")

cursor.execute("""
INSERT INTO movies (name, year, score)
VALUES ('Avatar', 2023, 10.0)
""")

cursor.execute("""
INSERT INTO movies (name, year, score)
VALUES ('Velozes & Furiosos', 2023, 8.5)
""")    

# 4 - Gravando Dados no BD
connection.commit()
print('Dados inseridos com sucesso.')

# 5 - Fechando conexão
connection.close()