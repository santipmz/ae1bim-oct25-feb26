# Universitad Técnica Particular de Loja
# Carrera de Ingeniería en Tecnologías de Información
# Desarrollo Basado en Plataformas Web
# Santiago Patricio Muñoz Zurita

# configuracion.py

# Importación de clases y funciones
from sqlalchemy import create_engine # Función de conexión a la base de datos
from sqlalchemy.orm import sessionmaker # Función de creación de sesiones

# Define la Base de datos Sqlite
DATABASE_URL = "sqlite:///universidades.db"

# Crea la conexión a la base de datos
engine = create_engine(DATABASE_URL)

# Crea las sesiones
SessionLocal = sessionmaker(bind=engine)