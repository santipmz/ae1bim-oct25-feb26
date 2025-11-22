# Universitad Técnica Particular de Loja
# Carrera de Ingeniería en Tecnologías de Información
# Desarrollo Basado en Plataformas Web
# Santiago Patricio Muñoz Zurita

# consula_or.py

from sqlalchemy import or_
from configuracion import SessionLocal
from crear_base_entidades import Investigador
from presentacion import presentar

presentar()

session = SessionLocal()

res = session.query(Investigador).filter(
    or_(
        Investigador.nombre.like("%Santiago%"),
        Investigador.apellido.like("%Gómez%")
    )
).all()

for inv in res:
    print(inv.nombre, inv.apellido)

session.close()