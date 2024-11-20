from conexao import conn

cursor_obj = conn.cursor()
cursor_obj.execute("SELECT * FROM jogo")
result = cursor_obj.fetchall()
print(result)

