# Proyecto de Gestión de Libros

Este proyecto es una aplicación web para la gestión de libros que permite a los usuarios autenticarse, agregar, editar y eliminar libros. El frontend está desarrollado con React.js y el backend con FastAPI y PostgreSQL.


## Tabla de Contenidos

- [Características](#características)
- [Instalación](#instalación)
- [Uso](#uso)
- [Contribución](#contribución)

## Características

- Autenticación de usuarios
- Gestión de libros (agregar, editar, eliminar)
- Interfaz de usuario estilizada con daisyUI
- Enrutamiento en el frontend con React Router
- Conexión con backend utilizando Axios
- Gestión de estado con Context API

## Instalación

### Prerrequisitos

- Node.js
- Python 3.9+
- PostgreSQL

### Frontend

1. Clona el repositorio:

    ```bash
    git clone https://github.com/zvMateo/proyecto_final.git
    cd proyecto_final/client
    ```

2. Instala las dependencias:

    ```bash
    npm install
    ```

3. Crea un archivo `.env` en el directorio `client` con las variables de entorno necesarias:

    ```env
    VITE_API_BASE_URL=http://127.0.0.1:8000/api
    ```

4. Inicia la aplicación:

    ```bash
    npm run dev
    ```

### Backend

1. Navega al directorio `Api`:

    ```bash
    cd ../Api
    ```

2. Crea un entorno virtual y actívalo:

    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

3. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

4. Configura la base de datos PostgreSQL y ajusta el archivo `.env` con las variables de entorno necesarias:

    ```env
    DATABASE_URL=postgresql://[ingrese_aqui_su_usuario]:[su_contraseña]@localhost/[nombre_de_la_base_de_datos]
    ```

5. Inicia el servidor:

    ```bash
    uvicorn main:app --reload
    ```

## Uso

1. Navega a `http://localhost:5173/` en tu navegador.
2. Inicia sesión con las cuentas = "mateo@example.com" o "joa@example.com" y las contraseñas son = "mateo123" y "joa123"
3. Agrega, edita o elimina libros según sea necesario.

## Contribución

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-caracteristica`).
3. Realiza tus cambios y haz commit (`git commit -m 'Agrega nueva característica'`).
4. Sube tus cambios (`git push origin feature/nueva-caracteristica`).
5. Abre un Pull Request.
