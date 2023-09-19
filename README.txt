#API CREADA CON FLASK
#SQL ALCHEMY
#SQLITE #3
#PIPENV

#1. para iniciar app
    $pipenv install flask 
    $python app.py

#2. para manipular la base de datos
    $pipenv install Flask-SQLAlchemy

#3. para crear mi base de datos con sqlite3 
#   incluido en la libreria standar de Python
#   nombre de base de datos "starwars.db" dentro de carpeta "dataBase"
    $ sqlite3 dataBase/starwars.db
    sqlite> .databases
    sqlite> .exit

#4. CONSULTANDO TABLAS EN SQLITE
    $ sqlite3 dataBase/starwars.db 
    SQLite version 3.32.2 2021-07-12 15:00:17
    Enter ".help" for usage hints.
    sqlite> .table

#5. CREANDO TABLAS 
    $python
    >>>from app import db
    >>>db.create_all()

    ### ################# Ejemplo:
    >>> from app import db
    >>> db.create_all()
    >>>
    >>> exit()

    Alejo@ALEJO-PC MINGW64 ~/OneDrive/Documents/4GEEKS_PROJECTS/API_CRUD_REST_STARWARS (main)
    $ sqlite3 dataBase/starwars.db
    SQLite version 3.32.2 2021-07-12 15:00:17
    Enter ".help" for usage hints.
    sqlite> .tables
    favorites  users

6. crear end points  y metodos