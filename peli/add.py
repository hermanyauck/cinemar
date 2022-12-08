import peli

#duracion en minutos
#clasificacion 0 al 3
def add(titulo, duracion, clasificacion, idioma):
    conn = base.connect("base.db")
    cursor = conn.cursor()
    consulta = f'''INSERT INTO PELICULAS
    ("titulo","duracion","clasificacion","idioma")
    VALUES 
    ("{titulo}",{duracion},"{tipos.rest[clasificacion]}","{tipos.idiomas[idioma]}");'''
    cursor.execute(consulta)
    conn.commit()
    conn.close()
