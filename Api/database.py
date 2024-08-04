from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Carga las variables de entorno desde el archivo .env
load_dotenv()

# Obtén la URL de la base de datos desde las variables de entorno
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

# Motor de base de datos
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Clase que permite crear sesiones de base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Clase base de la que heredan las clases de modelo
Base = declarative_base()

# Función que devuelve una sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
