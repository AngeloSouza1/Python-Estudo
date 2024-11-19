import sqlite3


# 1 - Conectando no BD
connection = sqlite3.connect("titles.db")

# 2 - Criando um cursor
'''
Cursor é um interador que permite
navegar e manipular os do bd.
'''
cursor = connection.cursor()

# 3 - Criando a Tabela  
cursor.execute("""
CREATE TABLE movies (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        year INTEGER NOT NULL,
        score REAL NOT NULL
       );
""")

# 4 - Fechando conexão
print('Tabela criada com sucesso.')
# desconectando...
connection.close()
