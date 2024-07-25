from pydantic import BaseModel, EmailStr

class CreateUser(BaseModel):
    nombre: str
    email: EmailStr
    contraseña: str

class User(CreateUser):
    id: int

    class Config:
        from_attributes=True

class CreateBook(BaseModel):
    nombre: str
    descripcion: str
    propietario_id: int

class Book(CreateBook):
    id: int
    propietario_id: int

    class Config:
        from_attributes=True

# class BookUser(BaseModel):
#     nombre: str
#     descripcion: str


class UpdateBook(BaseModel):
    nombre: str
    descripcion: str
