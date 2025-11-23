# Universitad Técnica Particular de Loja
# Carrera de Ingeniería en Tecnologías de Información
# Desarrollo Basado en Plataformas Web
# Santiago Patricio Muñoz Zurita

# poblar_base.py

from configuracion import SessionLocal
from crear_base_entidades import Institucion, Departamento, Investigador, Publicacion

session = SessionLocal()

# Crear objetos tipo Institucion
inst1 = Institucion(
    nombre="Universidad Técnica Particular de Loja", 
    ciudad="Loja", 
    pais="Ecuador"
)
inst2 = Institucion(
    nombre="Escuela Politécnica Nacional", 
    ciudad="Quito", 
    pais="Ecuador"
)
inst3 = Institucion(
    nombre="Escuela Politécnica Salesiana", 
    ciudad="Cuenca", 
    pais="Ecuador"
)
inst4 = Institucion(
    nombre="Universidad de Los Andes", 
    ciudad="Bogotá", 
    pais="Colombia"
)
inst5 = Institucion(
    nombre="Escuela Latinoamericana de Medicina", 
    ciudad="La Habana", 
    pais="Cuba"
)
inst6 = Institucion(
    nombre="Universiada Politécnica del Litora", 
    ciudad="Guayaquil", 
    pais="Ecuador"
)
inst7 = Institucion(
    nombre="Universidad Politécnica de Madrid", 
    ciudad="Madrid", 
    pais="España"
)
inst8 = Institucion(
    nombre="Escuela Politécnica del Ejército", 
    ciudad="Sangolquí", 
    pais="Ecuador"
)
inst9 = Institucion(
    nombre="Kansas University", 
    ciudad="Kansas", 
    pais="Estados Unidos"
)
inst10 = Institucion(
    nombre="Massachusetts Techincal Institute", 
    ciudad="Cambridge", 
    pais="Estados Unidos"
)

session.add(inst1)
session.add(inst2)
session.add(inst3)
session.add(inst4)
session.add(inst5)
session.add(inst6)
session.add(inst7)
session.add(inst8)
session.add(inst9)
session.add(inst10)
session.commit()

# Crear un departamento 
dep1 = Departamento(
    nombre="Departamento de Ciencias de la Computación", 
    codigo="DEP001",
    institucion=inst1
)
dep2 = Departamento(
    nombre="Departamento de Física", 
    codigo="DEP002",
    institucion=inst2
)
dep3 = Departamento(
    nombre="Departamento de Ciencias Sociales ", 
    codigo="DEP003",
    institucion=inst3
)
dep4 = Departamento(
    nombre="Departamento de Mecánica", 
    codigo="DEP004",
    institucion=inst4
)
dep5 = Departamento(
    nombre="Departamento de Medicina Aplicada",
    codigo="DEP005",
    institucion=inst5
)
dep6 = Departamento(
    nombre="Departamento de Investigación",
    codigo="DEP006",
    institucion=inst6
)
dep7 = Departamento(
    nombre="Departamento de TICS",
    codigo="DEP007",
    institucion=inst7
)

session.add(dep1)
session.add(dep2)
session.add(dep3)
session.add(dep4)
session.add(dep5)
session.add(dep6)
session.add(dep7)
session.commit()

# Crear un investigador
inv1 = Investigador(
    nombre="Santiago",
    apellido="Muñoz",
    email="spmunoz@utpl.edu",
    area_investigacion="Nuevas Tecnologías Agrícolas",
    departamento=dep1
)
inv2 = Investigador(
    nombre="Patricio",
    apellido="Zurita",
    email="pzurita@dominio.com",
    area_investigacion="Física Cuántica",
    departamento=dep2
)
inv3 = Investigador(
    nombre="Ezequiel",
    apellido="Rojas",
    email="ezerojasa@gnail.ec",
    area_investigacion="Filosofía del Copmportamiento",
    departamento=dep3
)
inv4 = Investigador(
    nombre="Paulina",
    apellido="Núñez",
    email="gatitapechocha@hotymail.es",
    area_investigacion="Turismo",
    departamento=dep4
)
inv5 = Investigador(
    nombre="Paquita",
    apellido="Serafina",
    email="pseraf@gmx.de.com",
    area_investigacion="Relaciones Laborales",
    departamento=dep5
)
inv6 = Investigador(
    nombre="Trajano",
    apellido="Adriano",
    email="emperor@romulus.it",
    area_investigacion="Redes de comunicaciones históricas",
    departamento=dep1
)
session.add(inv1)
session.add(inv2)
session.add(inv3)
session.add(inv4)
session.add(inv5)
session.add(inv6)
session.commit()

# Crear una publicación
pub1 = Publicacion(
    titulo="Plataforma de control de cultivos hidropónicos a través de la web",
    fecha_publicacion="2023-11-12",
    doi="11.2345/semconductores.ml",
    tipo_publicacion="Tesis",
    investigador=inv1
)
pub2 = Publicacion(
    titulo="Comportamiento de las partículas subatómicas en espacios simetricamente cerrados",
    fecha_publicacion="2025-11-12",
    doi="11.2345/semconductores.ml",
    tipo_publicacion="Artículo",
    investigador=inv2
)
pub3 = Publicacion(
    titulo="Filosofía aplicada al comportamiento infantil desde un punto de vista epistemológico",
    fecha_publicacion="2025-11-12",
    doi="11.2345/semconductores.ml",
    tipo_publicacion="Conferencia",
    investigador=inv3
)
pub4 = Publicacion(
    titulo="Factor de resistencia de materiales en aplicaciones turísticas",
    fecha_publicacion="2024-10-12",
    doi="11.2345/semconductores.ml",
    tipo_publicacion="Tesis",
    investigador=inv4
)
pub5 = Publicacion(
    titulo="Compilación de investigaciones novedosas en el ámbito laboral",
    fecha_publicacion="2025-09-12",
    doi="11.2345/semconductores.ml",
    tipo_publicacion="Artículo",
    investigador=inv5
)
pub6 = Publicacion(
    titulo="Redes de comunicaciones en la antigua Roma",
    fecha_publicacion="2025-08-12",
    doi="11.2345/semconductores.ml",
    tipo_publicacion="Conferencia",
    investigador=inv2
)

session.add(pub1)
session.add(pub2)
session.add(pub3)
session.add(pub4)
session.add(pub5)
session.add(pub6)
session.commit()

session.close()

print("Datos insertados correctamente.")