from fastapi import FastAPI, HTTPException, Depends, Query
from database import Base, engine, get_db
from models import BookModel, UserModel
from schemas import CreateUser, User, CreateBook, Book, UpdateBook
from typing import List
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy import func


Base.metadata.create_all(bind=engine)


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas las orígenes. Puedes restringir esto a dominios específicos.
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Permitir todos los encabezados
)

class LoginRequest(BaseModel):
    email: str
    contraseña: str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/api/login/")
def login(login_request: LoginRequest, db: Session = Depends(get_db)):
    normalized_email = login_request.email.lower()
    contraseña = login_request.contraseña
    user = db.query(UserModel).filter(func.lower(UserModel.email) == normalized_email).first()
    if user is None or not user.check_password(contraseña):
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")
    return user


@app.get("/api/users",response_model=List[User])
async def read_all_user(db=Depends(get_db)):
    users = db.query(UserModel).all()
    return users



# Ruta para crear un nuevo usuario
@app.post("/api/users/", response_model=User)
def create_user(user: CreateUser, db: Session = Depends(get_db)):
    normalized_email = user.email.lower()
    db_user = UserModel(email=normalized_email, password=user.password)
    db_user.set_password(user.contraseña)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user



@app.put("/api/users/{user_id}", response_model=User)
def update_user(user_id: int, updated_user: CreateUser, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no registrado")
    user.email = updated_user.email
    user.contraseña = updated_user.contraseña
    db.commit()
    db.refresh(user)
    return user

@app.delete("/api/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no registrado")
    db.delete(user)
    db.commit()
    return {"message": "El usuario ha sido eliminado con éxito"}


@app.get("/api/libros", response_model=List[Book])
async def read_all_books(
    db: Session = Depends(get_db),
    skip: int = Query(0, alias="skip"),
    limit: int = Query(10, alias="limit")
):
    books = db.query(BookModel).offset(skip).limit(limit).all()
    return books



# Ruta para crear un nuevo libro para un usuario específico
@app.post("/api/libros/", response_model=Book)
def create_book(book: CreateBook, db: Session = Depends(get_db)):
    propietario = db.query(UserModel).filter(UserModel.id == book.propietario_id).first()
    if not propietario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    db_book = BookModel(nombre=book.nombre, descripcion=book.descripcion, propietario_id=book.propietario_id)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book
#

# Ruta para obtener todos los libros de un usuario específico
@app.get("/api/users/{user_id}/libros/", response_model=List[Book])
def read_books_by_user(
    user_id: int,
    db: Session = Depends(get_db),
    skip: int = Query(0, alias="skip"),
    limit: int = Query(10, alias="limit")
):
    libros = db.query(BookModel).filter(BookModel.propietario_id == user_id).offset(skip).limit(limit).all()
    return libros

@app.put("/api/libros/{libro_id}", response_model=Book)
def update_libro(libro_id: int, book: UpdateBook, db: Session = Depends(get_db)):
    db_book = db.query(BookModel).filter(BookModel.id == libro_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    
    db_book.nombre = book.nombre
    db_book.descripcion = book.descripcion
    
    db.commit()
    db.refresh(db_book)
    return db_book

@app.delete("/api/libros/{libro_id}", status_code=204)
def delete_libro(libro_id: int, db: Session = Depends(get_db)):
    db_book = db.query(BookModel).filter(BookModel.id == libro_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    
    db.delete(db_book)
    db.commit()
    return {"message": "Libro eliminado exitosamente"}
