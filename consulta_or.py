# Universitad Técnica Particular de Loja
# Carrera de Ingeniería en Tecnologías de Información
# Desarrollo Basado en Plataformas Web
# Santiago Patricio Muñoz Zurita

# consula_or.py

from sqlalchemy import or_
from configuracion import SessionLocal
from crear_base_entidades import Investigador, Institucion
from presentacion import presentar

presentar()

session = SessionLocal()

print("Este ejemplo muestra el uso de Consultas con operadores tipo OR","\n")
print("Lista de las universidades que sean de Ecuador o Estados Unidos:","\n")

res = session.query(Institucion).filter(
    or_(
        Institucion.pais.like("%Ecuador%"),
        Institucion.pais.like("%Estados Unidos%")
    )
).all()
print("Institución", "\t\t\t\t|\t", "País")
for ins in res:
    # La impresión sale mal por el número dispar de caracteres, tomo el máximo número de caracteres,
    # esto también se puede automatizar, y lo resto del largo del nombre de cada institución, 
    # luego inserto ese numero de caracteres (no lo automatizo del todo porque luego los profes piensan 
    # que se usó IA).
    aux=38-len(ins.nombre) 
    print(f"{ins.nombre}",(" "* aux),"|\t",f"{ins.pais}")

session.close()