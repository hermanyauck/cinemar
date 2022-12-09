import user
import gui
import peli
import funciones
import sqlite3
import sqlite

usuario = gui.login()

if (usuario[2] == "admin"):
    gui.admin()