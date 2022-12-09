import funciones
import sqlite3
import sqlite

def funcion(pelicula, sala, fecha, hora):
    pass

def sala(asientos):
    sqlite.insert(f'''INSERT INTO SALAS 
    (butacas) VALUES 
    ("{asientos}");''')

def funcion(pelicula, sala, anio, mes, dia, hora):
    fecha = anio + mes + dia
    sqlite.insert(f'''INSERT INTO FUNCIONES
    (idPelicula, idSala, fecha, hora)
    VALUES
    ("{pelicula}","{sala}","{fecha}","{hora}";''')

