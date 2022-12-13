from tkinter import *
from tkinter import messagebox

import peli.add
from gui import dUsuario

def getPeli():
    et = entryTitulo.get()
    ed = entryDuracion.get()
    er = entryRestriccion.get()
    peli.add.add(et, ed, er)


def addPeli():
    global entryTitulo
    global entryDuracion
    global entryRestriccion
    wPeli = Toplevel(wAdmin)
    wPeli.title("AGREGAR PELICULA")
    wPeli.geometry("300x250")
    entryTitulo = StringVar()
    entryDuracion = StringVar()
    entryRestriccion = StringVar()
    Label(wPeli, text="titulo").place(x=30, y=50)
    Label(wPeli, text="duracion").place(x=30, y=90)
    Label(wPeli, text="restriccion").place(x=30, y=130)
    Entry(wPeli, textvariable=entryTitulo).place(x=100, y=50)
    Entry(wPeli, textvariable=entryDuracion).place(x=100, y=90)
    Entry(wPeli, textvariable=entryRestriccion).place(x=100, y=130)
    Button(wPeli, text="Cargar", command=lambda: getPeli()).place(x=100, y=170)

def addUser():
    global entryName
    global entryEdad
    global entryUser
    global entryPassword
    global sbmitbtn
    wAddUser = Toplevel(wAdmin)
    wAddUser.title("AGREGAR USUARIO")
    wAddUser.geometry("300x250")
    entryName = StringVar()
    entryEdad = StringVar()
    entryUser = StringVar()
    Label(wAddUser, text="titulo").place(x=30, y=50)
    Label(wAddUser, text="duracion").place(x=30, y=90)
    Label(wAddUser, text="restriccion").place(x=30, y=130)
    Label(wAddUser, text="restriccion").place(x=30, y=130)
    Entry(wAddUser, textvariable=entryTitulo).place(x=100, y=50)
    Entry(wAddUser, textvariable=entryDuracion).place(x=100, y=90)
    Entry(wAddUser, textvariable=entryRestriccion).place(x=100, y=130)
    sbmitbtn = Button(wAddUser, text="Cargar", command=lambda: getPeli()).place(x=100, y=170)



def addFunc():
    pass
def addResv():
    pass
def salir():
    pass

wAdmin = Tk()
wAdmin.title('CINEMAR ADMIN')
wAdmin.geometry("800x600")
btbAddPeli = Button(wAdmin, text="Agregar Pelicula", command=lambda: addPeli()).place(x=250, y=100)
btbAddUser = Button(wAdmin, text="Agregar Usuario", command=lambda: addUser()).place(x=250, y=150)
btbAddFunc = Button(wAdmin, text="Agregar Funcion", command=lambda: addFunc()).place(x=250, y=200)
btbAddResv = Button(wAdmin, text="Agregar Reserva", command=lambda: addResv()).place(x=250, y=250)
btbAddSali = Button(wAdmin, text="Salir y cerrar sesion", command=lambda: salir()).place(x=240, y=300)
wAdmin.mainloop()