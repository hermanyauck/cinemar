import user.add
import user.listar
import sqlite
import sqlite3

puestos = ("client", "vendor", "admin")
dpuestos = {0:"client", 1:"vendor", 2:"admin"}

def getUser(us, pas):
    salida = [False, False]
    #user y pass
    usp = sqlite.selects(f'''select 
    usuario, password, puesto, nombre, edad, puesto
    FROM PERSONAS 
    WHERE usuario = "{us}"''')
    try:
        uspp = usp[0]
        if(us == uspp[0]):
            salida[0] = uspp[0]
            if uspp[1] == pas:
                salida[1] = uspp[1]
                salida.append(uspp[2])
                salida.append(uspp[3])
                salida.append(uspp[4])
                salida.append(uspp[5])
    finally:
        return salida


class usuario:
    def __init__(self, nombre, edad, usuario, password, puesto):
        self.nombre = nombre
        self.edad = edad
        self.usuario = usuario
        self.password = password
        self.puesto = puesto
    #def __init__(self, lista):

    @property
    def nombre(self):
        return self.nombre
    @property
    def edad(self):
        return self.edad
    @property
    def usuario(self):
        return self.usuario
    @property
    def password(self):
        return self.password
    @property
    def puesto(self):
        return self.puesto
    @nombre.setter
    def nombre(self,addNombre):
        self.nombre = addNombre
    @edad.setter
    def edad(self, addEdad):
        self.edad = addEdad
    @usuario.setter
    def usuario(self, addUsuario):
        self.usuario = addUsuario
    @password.setter
    def password(self, addPass):
        self.password = addPass
    @puesto.setter
    def puesto(self,addPuesto):
        self.puesto = addPuesto
