1. Preparar MySQL 
En MySQL con (Xammp o MySqlWorkBench):

CREATE DATABASE tareasdb;
CREATE USER 'todo_user'@'localhost' IDENTIFIED BY 'password123';
GRANT ALL PRIVILEGES ON tareasdb.* TO 'todo_user'@'localhost';
FLUSH PRIVILEGES;


No necesitas crear la tabla: models.Base.metadata.create_all() la crea sola.

2. En VSCode:
   Ve a la terminal o Abres nueva terminal (new terminal)

   escribe el siguiente comando:
   pip install fastapi uvicorn mysql-connector-python pydantic


   luego el siguiente comando:

   uvicorn main:app --reload


   Luego ve a tu navegador web (Mozilla, Chrome, edge u otro) y en barra de navegación escribe:

   http://127.0.0.1:8000/docs

   
4. Abrir el frontend
Abre frontend/index.html directamente, ( En la carpeta de tu proyecto abre la página web index.html )


o
Usa un server estático (ej. extensión Live Server de VSCode).
Si usas Live Server, suele correr en http://127.0.0.1:5500 (ya permitido en CORS).
   
