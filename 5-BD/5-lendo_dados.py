import sqlite3

# 1 - Conectando no BD
connection = sqlite3.connect("movies.db")

# 2 - Criando um cursor
'''
Cursor é um interador que permite
navegar e manipular os do bd.
'''
cursor = connection.cursor()

# 3 - Lendo Dados
data = cursor.execute("""
SELECT * FROM movies
""")
print(data.fetchall())

# 4 - Iterando os Dados
for row in cursor.execute("SELECT * FROM movies"):
    print(f"{row}\n")
    
# 5 - Ordenando pelo Score
print("\\nFilmes Ordenados pelo Score\\n")
for row in cursor.execute("SELECT * FROM movies ORDER BY score desc"):
    print(f"{row}")

# 6 - Fechando conexão
connection.close()