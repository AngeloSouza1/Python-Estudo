from conexao import conn

cursor_obj = conn.cursor()

sql = """ UPDATE game
                SET name = %s
                WHERE id = %s"""
                
cursor_obj.execute(sql, ("Mario World 2", 5))

conn.commit()

conn.close()


