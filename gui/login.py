from tkinter import *
from tkinter import messagebox
from gui import dUsuario
import user

def getUss():
    eu = entryUser.get()
    ep = entryPass.get()
    usuario = user.getUser(eu,ep)
    if not(usuario[0]):
        messagebox.showinfo(message='usuario no existe')
    elif not(usuario[1]):
        messagebox.showinfo(message='password incorrecta')
    else:
        messagebox.showinfo(message=f'ingresar como {usuario[3]}')
        root.quit()
        dUsuario.extend(usuario)
    return

root = Tk()
root.title('CINEMAR LOGIN')
root.geometry("800x600")

entryUser = StringVar()
entryPass = StringVar()

usuario = Label(root, text="usuario").place(x=30, y=50)
password = Label(root, text="password").place(x=30, y=90)
eUser = Entry(root, textvariable=entryUser).place(x=100, y=50)
ePass = Entry(root, show="*", textvariable=entryPass).place(x=100, y=90)
sbmitbtn = Button(root, text="Entrar", command=lambda: getUss()).place(x=90, y=130)

root.mainloop()