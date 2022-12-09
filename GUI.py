import tkinter as tk
from tkinter import *


top = tk.Tk()
top.geometry("800x600")
usuario = Label(top, text="usuario").place(x=30, y=50)
password = Label(top, text="password").place(x=30, y=90)

sbmitbtn = Button(top, text="Entrar").place(x=30, y=170)

eUser = Entry(top).place(x=80, y=50)
ePass = Entry(top, show="*").place(x=80, y=90)


top.mainloop()