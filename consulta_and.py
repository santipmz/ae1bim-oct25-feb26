# Universitad Técnica Particular de Loja
# Carrera de Ingeniería en Tecnologías de Información
# Desarrollo Basado en Plataformas Web
# Santiago Patricio Muñoz Zurita

# consula_and.py

from sqlalchemy import and_
from configuracion import SessionLocal
from crear_base_entidades import Publicacion, Investigador
from presentacion import presentar

presentar()

session = SessionLocal()

print("Este ejemplo muestra el uso de Consultas con operadores tipo AND","\n")
print("Lista de las publicaciónes de Patricio Zurita con fecha mayor al 1 de noviembre de 2025:","\n")

res = session.query(Publicacion).join(Investigador).filter(
    and_(
        Investigador.apellido == "Zurita",
        Publicacion.fecha_publicacion >= "2025-11-01"
    )
).all()
print("Título", "\t\t\t\t\t\t\t\t\t\t\t|\t", "Fecha de publicación")
for pub in res:
    print(pub.titulo,"\t|\t", pub.fecha_publicacion)

session.close()
