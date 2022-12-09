from tkinter import *
from tkinter import messagebox
from gui import dUsuario

def addPeli():


root = Tk()
root.title('CINEMAR ADMIN')
root.geometry("800x600")
sbmitbtn = Button(root, text="Entrar", command=lambda: getUss()).place(x=90, y=130)

root.mainloop()