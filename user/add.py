import sqlite3 as base

puestos = ("client", "vendor", "admin")
def agregar(nombre, edad, usuario, password, tipo):
    conn = base.connect("base.db")
    cursor = conn.cursor()
    consulta = f'''INSERT INTO PERSONAS
    ("nombre","edad","usuario","password","puesto")
    VALUES 
    ("{nombre}",{edad},"{usuario}","{password}","{tipo}");'''
    cursor.execute(consulta)
    conn.commit()
    conn.close()

def client(nombre, edad, usuario, password):
    agregar(nombre, edad, usuario, password, puestos[0])

def vendor(nombre, edad, usuario, password):
    agregar(nombre, edad, usuario, password, puestos[1])

def admin(nombre, edad, usuario, password):
    agregar(nombre, edad, usuario, password, puestos[2])
