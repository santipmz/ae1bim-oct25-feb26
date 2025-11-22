# Universitad Técnica Particular de Loja
# Carrera de Ingeniería en Tecnologías de Información
# Desarrollo Basado en Plataformas Web
# Santiago Patricio Muñoz Zurita

# consula_all.py

from configuracion import SessionLocal
from crear_base_entidades import Institucion
from presentacion import presentar

presentar()

session = SessionLocal()

instituciones = session.query(Institucion).all()
for inst in instituciones:
    print(inst.nombre)

session.close()