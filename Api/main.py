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
# @app.post("/api/libros/", response_model=Book)
# def create_book(book: CreateBook, propietario_id: int, db: Session = Depends(get_db)):
#     propietario = db.query(UserModel).filter(UserModel.id == propietario_id).first()
#     if not propietario:
#         raise HTTPException(status_code=404, detail="Usuario no encontrado")
#     db_book = BookModel(nombre=book.nombre, descripcion=book.descripcion, propietario_id=propietario_id)
#     db.add(db_book)
#     db.commit()
#     db.refresh(db_book)
#     return db_book


# @app.post("/api/libros/", response_model=Book)
# def create_book(book: CreateBook, propietario_id: int, db: Session = Depends(get_db)):
#     propietario = db.query(UserModel).filter(UserModel.id == propietario_id).first()
#     if not propietario:
#         raise HTTPException(status_code=404, detail="Usuario no encontrado")
#     db_book = BookModel(nombre=book.nombre, descripcion=book.descripcion, propietario_id=propietario_id)
#     db.add(db_book)
#     db.commit()
#     db.refresh(db_book)
#     return db_book



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
# @app.post("/api/libro/", status_code=HTTP_201_CREATED, response_model=Book)
# async def create_book(new_book:CreateBook, db=Depends(get_db)):
#     book = BookModel(**new_book.model_dump())
#     db.add(book)
#     db.commit()
#     db.refresh(book)
#     return book


    # @app.get("/api/libros/", response_model=List[BookSchema], status_code=HTTP_200_OK)
    # def read_all_libros():
    #     data = conn.read_all_libros()
    #     items = [{"id": entry[0], "nombre": entry[1], "descripcion": entry[2], "propietario_id": entry[3]} for entry in data]
    #     return items


    # @app.get("/api/libro/{libro_id}", response_model=BookSchema, status_code=HTTP_200_OK)
    # def read_one_libro(libro_id: int):
    #     data = conn.read_one_libro(libro_id)
    #     if not data:
    #         raise HTTPException(status_code=404, detail="Libro no encontrado")
    #     return {"id": data[0], "nombre": data[1], "descripcion": data[2], "propietario_id": data[3]}


    # @app.post("/api/libro/", response_model=BookSchema, status_code=HTTP_201_CREATED)
    # def create_libro(libro: BookSchema):
    #     data = libro.model_dump()
    #     data.pop("id", None)
    #     conn.write_libro(data)
    #     return Response(status_code=HTTP_201_CREATED)


    # @app.put("/api/libro/{libro_id}", response_model=BookSchema, status_code=HTTP_200_OK)
    # def update_libro(libro_id: int, libro: BookSchema):
    #     data = libro.model_dump()
    #     data["id"] = libro_id
    #     conn.update_libro(data)
    #     return libro


    # @app.delete("/api/libro/{libro_id}", status_code=HTTP_204_NO_CONTENT)
    # def delete_libro(libro_id: int):
    #     conn.delete_libro(libro_id)
    #     return Response(status_code=HTTP_204_NO_CONTENT)


# from fastapi import FastAPI, HTTPException, Response
# from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT
# from typing import Union,Optional,List
# from models.user_connection import UserConnection
# from pydantic import BaseModel, EmailStr


# app = FastAPI()
# conn = UserConnection()

# class LoginSchema(BaseModel):
#     email: EmailStr
#     contraseña: str


# class UserSchema(BaseModel):
#     id: Optional[int]
#     nombre: str
#     email: EmailStr
#     contraseña: str

# class BookSchema(BaseModel):
#     id: Optional[int]
#     nombre: str
#     descripcion: str
#     propietario_id: int

# #Operaciones CRUD para usuarios
# @app.get("/api/users", response_model=List[UserSchema], status_code=HTTP_200_OK)
# def read_all_user():
#     data = conn.read_all_user()
#     items = [{"id": entry[0], "nombre": entry[1], "email": entry[2], "contraseña": entry[3]} for entry in data]
#     return items

#     # items = []
#     # for entry in data:
#     #     dictionary = {
#     #         "id": entry[0],
#     #         "nombre": entry[1],
#     #         "email": entry[2],
#     #         "contraseña": entry[3],
#     #     }
#     #     items.append(dictionary)
#     # return items


# # @app.get("/", status_code=HTTP_200_OK)
# # def read_root():
# #     data = conn.read_all()
# #     items = []
# #     for entry in data:
# #         dictionary = {
# #             "id":entry[0],
# #             "nombre":entry[1],
# #             "email":entry[2],
# #             "contraseña":entry[3],
# #         }
# #         items.append(dictionary)
# #     return items

# @app.get("/api/user/{user_id}", response_model=UserSchema, status_code=HTTP_200_OK)
# def read_user(user_id:int):
#     data = conn.read_one_user(user_id)
#     if not data:
#         raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
#     return {"id": data[0], "nombre": data[1], "email": data[2], "contraseña": data[3]}
#     # dictionary = {
#     #         "id":data[0],
#     #         "nombre":data[1],
#     #         "email":data[2],
#     #         "contraseña":data[3],
#     # }
#     # return dictionary


# # @app.get("/api/libros/{libro_id}", response_model=BookSchema, status_code=HTTP_200_OK)
# # def read_libro(libro_id: int):
# #     data = conn.read_one_libro(libro_id)
# #     if not data:
# #         raise HTTPException(status_code=404, detail="Libro no encontrado")
# #     dictionary = {
# #         "id": data[0],
# #         "nombre": data[1],
# #         "descripcion": data[2],
# #         "propietario_id": data[3],
# #     }
# #     return dictionary



# @app.post("/api/user/", response_model=UserSchema, status_code=HTTP_201_CREATED)
# def create_user(user:UserSchema):
#     data = user.model_dump()
#     data.pop("id", None)
#     conn.write_user(data)
#     return user
#     # return Response(status_code=HTTP_201_CREATED)


# @app.put("/api/user/{user_id}", response_model=UserSchema, status_code=HTTP_200_OK)
# def update_user(user_id:int, user: UserSchema):
#     data = user.model_dump()
#     data["id"] = user_id
#     conn.update_user(data)
#     return user
#     # return Response(status_code=HTTP_200_OK)

# # @app.put("/api/libros/{libro_id}", response_model=BookSchema, status_code=HTTP_200_OK)
# # def update_libro(libro_id: int, libro: BookSchema):
# #     data = libro.model_dump()
# #     data["id"] = libro_id
# #     conn.update_libro(data)
# #     return Response(status_code=HTTP_200_OK)

# @app.delete("/api/user/{user_id}", status_code=HTTP_204_NO_CONTENT)
# def delete_user(user_id:int):
#     conn.delete_user(user_id)
#     return Response(status_code=HTTP_204_NO_CONTENT)

# # @app.delete("/api/libros/{libro_id}", status_code=HTTP_204_NO_CONTENT)
# # def delete_libro(libro_id: int):
# #     conn.delete_libro(libro_id)
# #     return Response(status_code=HTTP_204_NO_CONTENT)


# # Operaciones CRUD para libros
# @app.get("/api/libros/", response_model=List[BookSchema], status_code=HTTP_200_OK)
# def read_all_libros():
#     data = conn.read_all_libros()
#     items = [{"id": entry[0], "nombre": entry[1], "descripcion": entry[2], "propietario_id": entry[3]} for entry in data]
#     return items

#     # items = []
#     # for entry in data:
#     #     dictionary = {
#     #         "id": entry[0],
#     #         "nombre": entry[1],
#     #         "descripcion": entry[2],
#     #         "propietario_id": entry[3],
#     #     }
#     #     items.append(dictionary)
#     # return items

# @app.post("/api/libro/", response_model=BookSchema, status_code=HTTP_201_CREATED)
# def create_libro(libro: BookSchema):
#     data = libro.model_dump()
#     data.pop("id", None)
#     conn.write_libro(data)
#     return Response(status_code=HTTP_201_CREATED)


# # @app.post("/api/libro/", response_model=BookSchema, status_code=HTTP_201_CREATED)
# # def create_libro(libro: BookSchema):
# #     data = libro.model_dump(exclude_unset=True)
# #     if "descripcion" not in data or not data["descripcion"]:
# #         raise HTTPException(status_code=400, detail="El campo 'descripcion' es obligatorio")
# #     data.pop("id", None)
# #     conn.write_libro(data)
# #     return libro
# #     # return Response(status_code=HTTP_201_CREATED)



# @app.get("/api/libro/{libro_id}", response_model=BookSchema, status_code=HTTP_200_OK)
# def read_one_libro(libro_id: int):
#     data = conn.read_one_libro(libro_id)
#     if not data:
#         raise HTTPException(status_code=404, detail="Libro no encontrado")
#     return {"id": data[0], "nombre": data[1], "descripcion": data[2], "propietario_id": data[3]}
#     # dictionary = {
#     #     "id": data[0],
#     #     "nombre": data[1],
#     #     "descripcion": data[2],
#     #     "propietario_id": data[3],
#     # }
#     # return dictionary

# @app.put("/api/libro/{libro_id}", response_model=BookSchema, status_code=HTTP_200_OK)
# def update_libro(libro_id: int, libro: BookSchema):
#     data = libro.model_dump()
#     data["id"] = libro_id
#     conn.update_libro(data)
#     return libro
#     # return Response(status_code=HTTP_200_OK)

# @app.delete("/api/libro/{libro_id}", status_code=HTTP_204_NO_CONTENT)
# def delete_libro(libro_id: int):
#     conn.delete_libro(libro_id)
#     return Response(status_code=HTTP_204_NO_CONTENT)