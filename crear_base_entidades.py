# Universitad Técnica Particular de Loja
# Carrera de Ingeniería en Tecnologías de Información
# Desarrollo Basado en Plataformas Web
# Santiago Patricio Muñoz Zurita

# crear_base_entidad.py

from sqlalchemy import *
from sqlalchemy.orm import declarative_base, relationship
from configuracion import engine

# Clase base para los modelos ORM
Base = declarative_base()

class Institucion(Base):
    __tablename__ = "institucion"

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    ciudad = Column(String, nullable=False)
    pais = Column(String, nullable=False)

    # Relación 1 a muchos con Departamento
    # Un Departamento tiene como atributo (clave foránea) una Institución.
    # Se usa las relaciones de POO en lugar del id
    departamentos = relationship("Departamento", back_populates="institucion")

class Departamento(Base):
    __tablename__ = "departamento"

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    codigo = Column(String, nullable=False)

    # Clave foránea a Institucion
    institucion_id = Column(Integer, ForeignKey("institucion.id"), nullable=False)
    institucion = relationship("Institucion", back_populates="departamentos")

    # Relación 1 a muchos con Investigador
    investigadores = relationship("Investigador", back_populates="departamento")

class Investigador(Base):
    __tablename__ = "investigador"

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    email = Column(String, nullable=False)
    area_investigacion = Column(String, nullable=False)

    # Clave foránea a Departamento
    departamento_id = Column(Integer, ForeignKey("departamento.id"), nullable=False)
    departamento = relationship("Departamento", back_populates="investigadores") 

    # Relación 1 a muchos con Publicacion
    publicaciones = relationship("Publicacion", back_populates="investigador")

class Publicacion(Base):
    __tablename__ = "publicacion"

    id = Column(Integer, primary_key=True)
    titulo = Column(String, nullable=False)
    # El enunciado pide formato 'YYYY-MM-DD' en cadena, así que se usa String
    fecha_publicacion = Column(String, nullable=False)
    doi = Column(String, nullable=False)
    tipo_publicacion = Column(String, nullable=False)

    # Clave foránea a Investigador
    investigador_id = Column(Integer, ForeignKey("investigador.id"), nullable=False)
    investigador = relationship("Investigador", back_populates="publicaciones") 


if __name__ == "__main__":
    # Se crea físicamente las tablas en la base de datos
    Base.metadata.create_all(engine)
    print("Base de datos y tablas creadas correctamente.")
