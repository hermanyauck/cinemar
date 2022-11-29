import sqlite3 as base

usuarios = []

def usuarios():
    conn = base.connect("base.db")
    cursor = conn.cursor()
    consulta = f'''INSERT INTO PELICULAS
    ("titulo","duracion","clasificacion","idioma")
    VALUES 
    ("{titulo}",{duracion},"{tipos.rest[clasificacion]}","{tipos.idiomas[idioma]}");'''
    cursor.execute(consulta)
    conn.commit()
    conn.close()