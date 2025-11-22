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

res = session.query(Publicacion).join(Investigador).filter(
    and_(
        Investigador.id == 1,
        Publicacion.fecha_publicacion >= "2025-11-01"
    )
).all()

for pub in res:
    print(pub.titulo, pub.fecha_publicacion)

session.close()
