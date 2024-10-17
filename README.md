# No-Country-Back-End

## Tabla de Contenidos

- [Instalación](#instalación)
- [Uso](#uso)
- [Endpoints](#endpoints)
    - [Usuarios](#usuarios)

## Instalación

### Prerrequisitos

Antes de comenzar, asegúrate de tener instalado lo siguiente en tu sistema:

- Python (versión 3.12.2)
- PostgreSQL (versión 16)
- pip (administrador de paquetes de Python)

### Pasos de Instalación

1. **Clona este repositorio:**

```bash
git clone https://github.com/Daniheto/No-Country-Back-End.git
```

2. **Crear el entorno virtual:**

Utiliza `virtualenv` o otro gestor de entornos virtuales

```bash
pip install virtualenv
python -m virtualenv venv
```

3. **Instalar las dependencias:**

```bash
cd No-Country-Back-End
pip install -r requirements.txt
```

4. **Configurar variables de entorno:**

- Crea una base de datos PostgreSQL en tu entorno.
- Crea un archivo `.env` en la ruta raiz de tu proyecto y crea las variables de entorno con los datos correpodientes:
    - `ENGINE` -> Tipo de base de datos
    - `NAME` -> Nombre de la base de datos
    - `USER` -> Usuario de la base de datos
    - `PASSWORD` -> Contraseña de la base de datos
    - `HOST` -> Host de la base de datos
    - `PORT` -> Puerto de la base de datos
- En el archivo `.env` crea una nueva variable para la conexion del host del fronted:
    - `HOST_FRONTEND` -> URL del frontend

5. **Crea las migraciones:**

```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Ejecutar el servidor:**

```bash
python manage.py runserver
```

¡Listo! El proyecto ahora debería estar en funcionamiento en tu entorno local. Puedes acceder a él desde tu navegador web visitando `http://localhost:8000`.

## Endpoints

### Usuarios

| Nombre | Método | Url | Descripción |
|:------ | :----- | :-- | :---------- |
| [Registro de Usuarios](#registro-de-usuario) | `POST` | `/api/users/sign_up` | Registro de usuarios. |
| [Inicio de Sesión de Usuarios](#inicio-de-sesión-de-usuario) | `POST` | `/api/users/sign_in` | Inicio de sesión de los usuarios. |
| [Cierre de Sesión de Usuarios](#cierre-de-sesión-de-usuario) | `POST` | `/api/users/sign_out` | Cerrar sesión de un usuario autenticado. |
| [Actualización del Usuarios](#actualización-del-usuario) | `PUT` | `/api/users/update_user` | Actualizar la información del perfil del usuario. |
| [Eliminación del Usuarios](#eliminación-del-usuario) | `DELETE` | `/api/users/delete_user` | Eliminar el usuario actual. |

#### Registro de usuario

##### Método HTTP

```http
POST /api/users/sign_up
```

##### Parámetros

| Parámetro | Tipo     | Descripción                |
| :-------- | :------- | :------------------------- |
| `username` | `string` | **Requerido**. Nombre del usuario |
| `email` | `string` | **Requerido**.  Correo electrónico del usuario |
| `password` | `string` | **Requerido**. Contraseña del usuario |

##### Ejemplo de solicitud

```http
Content-Type: application/json

{
    "username": "testUsername",
    "email": "test@email.com",
    "password": "testPassword"
}
```

##### Ejemplo de respuesta exitosa

```http
HTTP/1.1 201 Created
Content-Type: application/json

{
    "status": "success",
    "message": "User registered successfully.",
    "data": {
        "token": {
            "token_key": "b14407b771de4372bb3fd864a7d4b12884b8db09"
        },
        "user": {
            "id": 1,
            "username": "testUsername",
            "email": "test@email.com",
            "date_joined": "2024-10-14T00:12:52.125524Z"
        }
    }
}
```

#### Inicio de sesión de usuario

##### Método HTTP

```http
POST /api/users/sign_in
```

##### Parámetros

| Parámetro | Tipo     | Descripción                |
| :-------- | :------- | :------------------------- |
| `username` | `string` | **Requerido**. Nombre del usuario |
| `password` | `string` | **Requerido**. Contraseña del usuario |

##### Ejemplo de solicitud

```http
Content-Type: application/json

{
    "username": "testUsername",
    "password": "testPassword"
}
```

##### Ejemplo de respuesta exitosa

```http
HTTP/1.1 201 Created
Content-Type: application/json

{
    "status": "success",
    "message": "User logged in successfully.",
    "data": {
        "token": {
            "token_key": "b14407b771de4372bb3fd864a7d4b12884b8db09",
            "token_expiration": "2024-10-17T23:50:09.865811+00:00"
        },
        "user": {
            "id": 1,
            "username": "testUsername",
            "email": "test@email.com",
            "date_joined": "2024-10-14T00:12:52.125524Z"
        }
    }
}
```

#### Cierre de sesión de usuario

##### Método HTTP

```http
POST /api/users/sign_out
```

##### Parámetros

| Parámetro | Tipo     | Descripción                |
| :-------- | :------- | :------------------------- |
| `Token` | `string` | **Requerido**. Token de autenticación |

##### Ejemplo de solicitud

```http
Content-Type: application/json
Authorization: Token <token>
```

##### Ejemplo de respuesta exitosa

```http
HTTP/1.1 200 Ok
Content-Type: application/json

{
    "status": "success",
    "message": "User logged out successfully."
}
```

#### Actualización del usuario

##### Método HTTP

```http
PUT /api/users/update_user
```

##### Parámetros

| Parámetro | Tipo     | Descripción                |
| :-------- | :------- | :------------------------- |
| `Token` | `string` | **Requerido**. Token de autenticación |
| `username` | `string` | **Requerido**. Nombre del usuario |
| `email` | `string` | **Requerido**.  Correo electrónico del usuario |
| `password` | `string` | **Requerido**. Contraseña del usuario |

##### Ejemplo de solicitud

```http
Content-Type: application/json
Authorization: Token <token>

{
    "username": "newUsername",
    "email": "new@email.com",
    "password": "newPassword"
}
```

##### Ejemplo de respuesta exitosa

```http
HTTP/1.1 200 Ok
Content-Type: application/json

{
    "status": "success",
    "message": "User logged out successfully."
}
```

#### Eliminación del usuario

##### Método HTTP

```http
DELETE /api/users/delete_user
```

##### Parámetros

| Parámetro | Tipo     | Descripción                |
| :-------- | :------- | :------------------------- |
| `Token` | `string` | **Requerido**. Token de autenticación |

##### Ejemplo de solicitud

```http
Content-Type: application/json
Authorization: Token <token>
```

##### Ejemplo de respuesta exitosa

```http
HTTP/1.1 200 Ok
Content-Type: application/json

{
    "status": "success",
    "message": "User deleted successfully."
}
```
