# Universitad Técnica Particular de Loja
# Carrera de Ingeniería en Tecnologías de Información
# Desarrollo Basado en Plataformas Web
# Santiago Patricio Muñoz Zurita

# consula_order.py

from configuracion import SessionLocal
from sqlalchemy import desc
from crear_base_entidades import Publicacion
from presentacion import presentar

presentar()

session = SessionLocal()
print("Este ejemplo muestra el uso de Consultas con operadores de Orden","\n")
print("Lista de publicaciones ordenadas por fecha:","\n")
pubs = session.query(Publicacion).order_by(Publicacion.fecha_publicacion).all()
print("Fecha de publicación", "\t|\t", "Título")
for p in pubs:
    print(p.fecha_publicacion, "\t\t|\t", p.titulo)

print("\nLista de publicaciones ordenadas por fecha descendente:","\n")
pubs = session.query(Publicacion).order_by(desc(Publicacion.fecha_publicacion)).all()
print("Fecha de publicación", "\t|\t", "Título")
for p in pubs:
    print(p.fecha_publicacion, "\t\t|\t", p.titulo)
session.close()