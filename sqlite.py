import sqlite3

def insert(consulta):
    conn = sqlite3.connect("base.db")
    cursor = conn.cursor()
    cursor.execute(consulta)
    conn.commit()
    conn.close()

def select(consulta):
    conn = sqlite3.connect("base.db")
    cursor = conn.cursor()
    cursor.execute(consulta)
    listas = cursor.fetchall()
    conn.commit()
    conn.close()
    return listas