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
    salida = cursor.execute(consulta)
    listas = salida.fetchall()
    conn.commit()
    conn.close()
    return listas