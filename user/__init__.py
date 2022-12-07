import user.add
import user.listar

puestos = ("client", "vendor", "admin")
import user

class usuario:
    def __init__(self, nombre, edad, usuario, password, puesto):
        self.nombre = ""
        self.edad = 0
        self.usuario = ""
        self.password = ""
        self.puesto = ""
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
