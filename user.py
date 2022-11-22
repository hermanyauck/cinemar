import sqlite3 as base

def addUser(nombre,edad,usuario,password):
    conn = base.connect("base.db")
    cursor = conn.cursor()
    consulta = f'''INSERT INTO PERSONAS
    ("nombre","edad","usuario","password")
    VALUES 
    ("{nombre}",{edad},"{usuario}","{password}");'''
    cursor.execute(consulta)
    conn.commit()
    conn.close()

addUser("herman",27,"herman95","123")