import sqlite
import sqlite3

usuarios = []

def usuarios():
    persona = sqlite.select('''SELECT 
    (nombre, edad, usuario, password, puesto) 
    FROM PERSONAS''')
    print(persona)