import user
import sqlite
import funciones

#user.add.client("adolecente","19","joven4","123")
#personas = sqlite.select("select * from PERSONAS")
#print(personas)
#user.listar.usuarios()

#peli.add.add("titulo", "140", 1, 2)

#funciones.add.sala("30")FALSE
#funciones.borrar.sala(2)

sal = user.getUser("herman95", "123")
print(sal)

if sal[0]:
    print(1)
else:
    print("no existe")