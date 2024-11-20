from conexao import conn

games = [
    ('Star Wars Survivor', 2023, 9.5),
    ('Samurai Shadow', 2010, 8.5)
]

# Usar 'with' para gerenciar a conexão e o cursor
with conn.cursor() as cursor:
    for game in games:
        cursor.execute(
            "INSERT INTO game (name, year, score) VALUES (%s, %s, %s)", 
            game
        )
    conn.commit()

print("Dados inseridos com sucesso!")
