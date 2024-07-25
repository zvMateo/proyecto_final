from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from security import hash_password, verify_password

class BookModel(Base):
    __tablename__ = "libros"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    descripcion = Column(String, index=True)
    propietario_id = Column(Integer, ForeignKey("usuarios.id"))

    propietario = relationship("UserModel", back_populates="libros")

class UserModel(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    contraseña = Column(String, index=True)

    def set_password(self, password: str):
        self.contraseña = hash_password(password)

    def check_password(self, password: str) -> bool:
        return verify_password(password, self.contraseña)

    libros = relationship("BookModel", back_populates="propietario")
