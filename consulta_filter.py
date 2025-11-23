# Universitad Técnica Particular de Loja
# Carrera de Ingeniería en Tecnologías de Información
# Desarrollo Basado en Plataformas Web
# Santiago Patricio Muñoz Zurita

# consula_filter.py

from configuracion import SessionLocal
from crear_base_entidades import Investigador
from presentacion import presentar

presentar()

session = SessionLocal()

print("Este ejemplo muestra el uso de Consultas con operadores con filter()","\n")
print("Lista de investigadores con Áreas de investigación que contenga \"Re\"","\n")

inv_re = session.query(Investigador).filter(
    Investigador.area_investigacion.like("%Re%")
).all()
print("Investigador", "\t\t\t\t|\t", "Área de Investigación")
for inv in inv_re:
    aux=33-len(inv.apellido+inv.nombre)+1 # Correccion de tamaños
    print(f"{inv.nombre} {inv.apellido}"," "*aux,"\t|\t",f"{inv.area_investigacion}")

session.close()
print("\nConsulta FILTER ejecutadas correctamente.")
