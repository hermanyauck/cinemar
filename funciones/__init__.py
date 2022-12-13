import funciones.add
import funciones.borrar
import sqlite

def listarSala():
    lista = sqlite.selects("SELECT id, butacas titulo FROM SALAS;")
    salida = list()
    for tuplas in lista:
        salida.append(f"sala: {tuplas[0]}, butacas: {tuplas[1]}")
    return salida

