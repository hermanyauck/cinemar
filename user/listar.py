import sqlite
import sqlite3

usuarios = []

#retorna una lista de tuplas
def usuarios():
    personas = sqlite.select('''SELECT 
    nombre, edad, usuario, password, puesto 
    FROM PERSONAS;''')
    print(personas)

