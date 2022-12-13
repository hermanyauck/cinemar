import sqlite3


def insert(consulta):
    conn = sqlite3.connect("base.db")
    cursor = conn.cursor()
    cursor.execute(consulta)
    conn.commit()
    conn.close()


def selects(consulta):
    conn = sqlite3.connect("base.db")
    cursor = conn.cursor()
    cursor.execute(consulta)
    listas = cursor.fetchall()
    conn.commit()
    conn.close()
    return listas


def select(consulta):
    listaDeTuplas = selects(consulta)
    lista = list()
    for tuplas in listaDeTuplas:
        lista.append(tuplas[0])
    return tuple(lista)


def borrar(tabla, condicion):
    conn = sqlite3.connect("base.db")
    cursor = conn.cursor()
    cursor.execute(f'''DELETE FROM {tabla} 
    WHERE {condicion}''')
    conn.commit()
    conn.close()
