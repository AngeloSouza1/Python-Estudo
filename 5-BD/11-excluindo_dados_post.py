from conexao import conn

cursor_obj = conn.cursor()

sql = """ DELETE FROM game
            WHERE id = %s"""
                
cursor_obj.execute(sql, (2,))

conn.commit()

print("Dado excluído com sucesso!")

conn.close()
