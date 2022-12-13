import peli.add
import sqlite

#restriccines
rest = ("G", "PG-13", "PG-16", "R")

#descriccion de restricciones
desc = {rest[0]:"audiencia genera",
        rest[1]:"orientación de los padres a menores de 13 años",
        rest[2]:"orientación de los padres a menores de 16 años",
        rest[3]:"acceso restringido a menores de edad"} #mas de 18

#edades minimas
edades = {rest[0]: 0,
          rest[1]: 13,
          rest[2]: 16,
          rest[3]: 18}

def listar():
    salida = sqlite.select("SELECT titulo FROM PELICULAS;")
    return salida
