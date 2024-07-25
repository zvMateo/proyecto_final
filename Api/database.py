from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "postgresql://postgres:password123@localhost/trabajo_final"


#Motor de base de datos
engine=create_engine(SQLALCHEMY_DATABASE_URL)

#Clase que permite crear sesiones de base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Clase base de la que heredan las clases de modelo
Base = declarative_base()

#Funcion que devuelve una sesion de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()