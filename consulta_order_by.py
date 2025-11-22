# Universitad Técnica Particular de Loja
# Carrera de Ingeniería en Tecnologías de Información
# Desarrollo Basado en Plataformas Web
# Santiago Patricio Muñoz Zurita

# consula_order.py

from configuracion import SessionLocal
from crear_base_entidades import Publicacion
from presentacion import presentar

presentar()

session = SessionLocal()

pubs = session.query(Publicacion).order_by(Publicacion.fecha_publicacion).all()
for p in pubs:
    print(p.fecha_publicacion, "-", p.titulo)

session.close()