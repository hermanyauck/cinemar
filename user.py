import sqlite3 as base

puestos = ("client", "vendor", "admin")

class add:
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
        add.agregar(nombre, edad, usuario, password, puestos[0])


add.client("teodoro","5","teo","123")