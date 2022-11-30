import sqlite3

def consulta(consulta):
    conn = sqlite3.connect("base.db")
    cursor = conn.cursor()
    cursor.execute(consulta)
    conn.commit()
    conn.close()