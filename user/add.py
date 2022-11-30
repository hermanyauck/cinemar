import user
import sqlite
import sqlite3

trupla = ("vacia")
def agregar(nombre, edad, usuario, password, tipo):
    try:
        sqlite.consulta(f'''INSERT INTO PERSONAS
        ("nombre","edad","usuario","password","puesto")
        VALUES 
        ("{nombre}",{edad},"{usuario}","{password}","{tipo}");''')

        #IntegrityError salta cuando no se cumple el unique
    except sqlite3.IntegrityError:
        print("ese usuario ya existe")

def client(nombre, edad, usuario, password):
    agregar(nombre, edad, usuario, password, user.puestos[0])

def vendor(nombre, edad, usuario, password):
    agregar(nombre, edad, usuario, password, user.puestos[1])

def admin(nombre, edad, usuario, password):
    agregar(nombre, edad, usuario, password, user.puestos[2])
