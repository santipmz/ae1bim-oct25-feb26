# Universitad Técnica Particular de Loja
# Carrera de Ingeniería en Tecnologías de Información
# Desarrollo Basado en Plataformas Web
# Santiago Patricio Muñoz Zurita

# consula_filter.py

from sqlalchemy import or_, and_
from configuracion import SessionLocal
from crear_base_entidades import Institucion, Departamento, Investigador, Publicacion
from presentacion import presentar

presentar()

session = SessionLocal()
print("CONSULTA 2: filter() investigadores del área IA")
inv_ia = session.query(Investigador).filter(
    Investigador.area_investigacion.like("%IA%")
).all()
for inv in inv_ia:
    print(f"{inv.nombre} {inv.apellido} - {inv.area_investigacion}")

    session.close()
print("\nConsulta FILTER ejecutadas correctamente.")
