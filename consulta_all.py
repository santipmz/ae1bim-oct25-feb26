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
print("Lista de todas las instituciones de Educación superior almaceadas:","\n")
instituciones = session.query(Institucion).all()
print("Identificador", "\t|\t", "Institución")
for inst in instituciones:
    print(inst.id,"\t\t|\t", inst.nombre)

session.close()