# No-Country-Back-End

## Tabla de Contenidos

- [Instalación](#instalación)
- [Uso](#uso)
- [Endpoints](#endpoints)

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
