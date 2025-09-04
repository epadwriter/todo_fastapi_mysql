from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import mysql.connector

# Configuración base de datos MySQL
db = mysql.connector.connect(
    host="localhost",
    user="todo_user",         # Cambiar si usas root
    password="password123",   # Tu contraseña
    database="tareasdb"
)

app = FastAPI()

# Habilitar CORS (para permitir que el frontend en otro servidor haga requests)
origins = [
    "http://127.0.0.1:5500",  # para pruebas locales (con Live Server en VSCode, por ejemplo)
    "http://localhost:5500",
    "https://www.midominio.com" # tu dominio real del frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo de datos
class Tarea(BaseModel):
    descripcion: str

@app.get("/tareas")
def obtener_tareas():
    cursor = db.cursor()
    cursor.execute("SELECT id, descripcion FROM tareas")
    resultados = cursor.fetchall()
    tareas = [{"id": fila[0], "descripcion": fila[1]} for fila in resultados]
    return tareas

@app.post("/tareas")
def agregar_tarea(tarea: Tarea):
    cursor = db.cursor()
    sql = "INSERT INTO tareas (descripcion) VALUES (%s)"
    cursor.execute(sql, (tarea.descripcion,))
    db.commit()
    return {"mensaje": "Tarea agregada"}

@app.delete("/tareas/{tarea_id}")
def borrar_tarea(tarea_id: int):
    cursor = db.cursor()
    sql = "DELETE FROM tareas WHERE id = %s"
    cursor.execute(sql, (tarea_id,))
    db.commit()
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return {"mensaje": "Tarea borrada"}
