import sqlite
import sqlite3

def sala(idSala):
    sqlite.borrar("SALAS", f"id = {idSala}")