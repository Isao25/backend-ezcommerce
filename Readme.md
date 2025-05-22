# **BACKEND EZCOMMERCE**
-------------------
## 1. Instalación de programas necesarios
### 1.1. Descargar e instalar python del sitio oficial
    https://www.python.org/
Verificamos que python esté instalado usando el siguiente comando en la consola de línea de comandos:

    python --version
    
Si nos sale la versión significa que está instalado correctamente.
### 1.2. Descargar e instalar Visual Studio Code del sitio oficial
    https://code.visualstudio.com/
### 1.3. Descargar e instalar  Postgresql del sitio oficial
Para este caso, estamos usando la versión 17 de postgresql.

    https://www.enterprisedb.com/downloads/postgres-postgresql-downloads
    
## 2. Preparar Postgresql:
### 2.1. Añadir variable de entorno
Una vez que tenemos instalado postgresql, añádelo a tus variables de entorno, para ello accede a las variables de entorno de Windows y en la sección "editar variables de entorno" agregas al PATH la ruta en la que se encuentra la carpeta "bin" de Postgresql. 
**Por ejemplo:**

    C:\Program Files\PostgreSQL\17\bin

### 2.2. Crear base de datos con Postgresql
2.2.1. Ejecutamos la consola de Postgresql: SQL Shell (psql), la cual se debería encontrar en la ruta en la que instaló postgresql.
**Por ejemplo:**

     C:\Program Files\PostgreSQL\17\scripts\runpsql.bat

2.2.2. En la consola, dejaremos las opciones por defecto y colocaremos una contraseña:
    
    Server [localhost]:
    Database [postgres]:
    Port [5432]:
    Username [postgres]:
    Contraseña para usuario postgres:

2.2.3. En la consola, creamos la base de datos para el sistema con el siguiente comando:

    create database ezcommercedb;

Luego, ejecutamos el comando:

    \l
El cual nos mostrará la lista de bases de datos, si en ella sale la base de datos que acabamos de crear, significa que todo salió correctamente.

## 3. Preparación del entorno:
### 3.1. Clonar el respositorio del backend usando GIT o descargándolo como .zip desde
    https://github.com/Isao25/backend-ezcommerce
### 3.2. Crear un entorno virtual
3.2.1. Abrir una consola de linea de comandos (CMD en Windows) en la ruta del repositorio clonado en el dispositivo.
3.2.2. Creamos un entorno virtual en la raíz del proyecto usando el siguiente comando:

    python -m virtualenv venv
3.2.3. activamos el entorno virtual usando el siguiente comando:

    .\venv\Scripts\activate

Notaremos que entramos al entorno virtual, la consola debería verse algo así:

    (venv) ruta\a\backend-ezcommerce>

## 3.3. Instalar dependencias
Para instalar todas las librerías y dependencias necesarias empleamos el siguiente comando y dentro del entorno virtual:

    pip install -r requirements.txt
    
# 4. Verificar contraseña
Abrimos el IDE Visual Studio Code e instalamos las extensiones correspondientes para python. 
Abrimos la carpeta BACKEND-EZCOMMERCE usando el menú File -> Open Folder y seleccionando la carpeta en la que se encuentra nuestro proyecto.
El árbol de directorios debe verse así:

    BACKEND-EZCOMMERCE/ 
    ├── epica1/
    ├── epica2/
    ├── epica4/
    ├── epica5/
    ├── epica6/
    ├── epica8/
    ├── ezcommerce/ 
    │   ├── settings.py  ← Archivo de configuración
    │   └── ...
    ├── scripts/
    │   └── seed_data.py  
    ├── venv/
    ├── .gitignore
    ├── manage.py
    ├── Readme.md
    └── requirements.txt

Abrimos el archivo settings.py (archivo de configuración) y nos dirigimos a esta sección:

    #Database Postgresql
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'ezcommercedb',
            'USER': 'postgres',
            'PASSWORD': 'virtualmiau16',  #←  Contraseña
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }

Acá debemos verificar que el usuario y la contraseña sean los mismos que colocamos cuando preparamos el entorno en la consola de Postgresql.
Una vez resuelto, procedemos a guardar los cambios y a levantar el servidor.

# 5. Levantar el servidor
## 5.1. Realizar Migraciones
Nos ubicamos en la consola que tiene el entorno virtual (venv) abierto y realizamos las migraciones correspondientes usando los comandos:

    python manage.py makemigrations
    python manage.py migrate

## 5.2. Ejecutar Seeder
Dentro del entorno virtual ejecutamos el seeder, el cual contiene datos iniciales para poder empezar a probar el sistema:

    python scripts\seed_data.py

La consola debería botar el siguiente mensaje indicando que todo salió bien:

    Datos iniciales insertados con éxito.

## 5.3. Levantar el servidor
Levantamos el servidor usando el comando:

    python manage.py runserver
  
 Nos debería salir los siguiente:
 
    (venv) ruta\a\backend-ezcommerce>python manage.py runserver
    Watching for file changes with StatReloader
    Performing system checks...
    
    System check identified no issues (0 silenced).
    May 22, 2025 - 00:26:40
    Django version 5.1.3, using settings 'ezcommerce.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CTRL-BREAK.

Con esto tendremos el servidor levantado. Procedemos a acceder al enlace en localhost:

    http://127.0.0.1:8000/

-------

# Notas finales:
## N1: 
Dependiendo de la versión de Windows y/o el terminal que decida utilizar (si el CMD o la terminal de Visual Studio Code), puede que tenga que cambiar los backslash '\' por slash '/' al ejecutar ciertos comandos.