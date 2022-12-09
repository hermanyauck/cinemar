import peli
import sqlite

#duracion en minutos
#clasificacion 0 al 3
def add(titulo, duracion, restriccion):
    sqlite.insert(f'''INSERT INTO PELICULAS
    ("titulo","duracion","restriccion")
    VALUES 
    ("{titulo}","{duracion}","{restriccion}");''')

