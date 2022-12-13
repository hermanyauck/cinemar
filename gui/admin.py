from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

import peli.add
import user.add
from user import puestos
from peli import listar as listPeli
from funciones import listarSala as listSala

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

def getUser():
    en = entryName.get()
    ee = entryEdad.get()
    eu = entryUser.get()
    eps = entryPassword.get()
    epu = entryPuesto.get()
    err = user.add.agregar(en, ee, eu, eps, epu)
    if not(err):
        messagebox.showinfo(message='usuario ya existe')

def addUser():
    global entryName
    global entryEdad
    global entryUser
    global entryPassword
    global entryPuesto
    wAddUser = Toplevel(wAdmin)
    wAddUser.title("AGREGAR USUARIO")
    wAddUser.geometry("300x340")
    entryName = StringVar()
    entryEdad = StringVar()
    entryUser = StringVar()
    entryPassword = StringVar()
    entryPuesto = StringVar()
    Label(wAddUser, text="nombre").place(x=30, y=50)
    Label(wAddUser, text="edad").place(x=30, y=90)
    Label(wAddUser, text="usuario").place(x=30, y=130)
    Label(wAddUser, text="contrasenia").place(x=30, y=170)
    Entry(wAddUser, textvariable=entryName).place(x=100, y=50)
    Entry(wAddUser, textvariable=entryEdad).place(x=100, y=90)
    Entry(wAddUser, textvariable=entryUser).place(x=100, y=130)
    Entry(wAddUser, textvariable=entryPassword).place(x=100, y=170)
    Radiobutton(wAddUser, text='Cliente', variable=entryPuesto, value=puestos[0]).place(x=75, y=200)
    Radiobutton(wAddUser, text='Vendedor', variable=entryPuesto, value=puestos[1]).place(x=75, y=230)
    Radiobutton(wAddUser, text='Admin', variable=entryPuesto, value=puestos[2]).place(x=75, y=260)
    Button(wAddUser, text="Cargar", command=lambda: getUser()).place(x=100, y=290)

def addFunc():
    wAddFunc = Toplevel(wAdmin)
    wAddFunc.title("AGREGAR FUNCION")
    wAddFunc.geometry("300x340")
    global entryPeli
    global entrySala
    global entryAnio
    global entryMes
    global entryDia
    entryPeli = StringVar()
    entrySala = StringVar()
    peliculas = listPeli()
    salas = listSala()
    Combobox(wAddFunc, textvariable=entryPeli, values=peliculas).place(x=30, y=50)
    Combobox(wAddFunc, textvariable=entrySala, values=salas).place(x=30, y=80)
    Button(wAddFunc, text="Cargar", command=lambda: print(entryPeli.get())).place(x=100, y=290)

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

