from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import random
from fastapi.middleware.cors import CORSMiddleware  # Importar CORSMiddleware

app = FastAPI()

# Habilitar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite solicitudes desde cualquier origen (cualquier puerto)
    allow_credentials=True,
    allow_methods=["*"],  # Permite cualquier tipo de método (GET, POST, etc.)
    allow_headers=["*"],  # Permite cualquier tipo de encabezado
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Datos de usuarios dummy
USUARIOS_DB = {
    "usuario1": {"password": "1234", "token": "token123"},
    "usuario2": {"password": "abcd", "token": "token456"}
}

# Modelo para el cuerpo del request del login
class Credenciales(BaseModel):
    usuario: str
    password: str

# Endpoint para iniciar sesión
@app.post("/login")
def login(credenciales: Credenciales):
    usuario = credenciales.usuario
    password = credenciales.password

    if usuario in USUARIOS_DB and USUARIOS_DB[usuario].get("password") == password:
        return {"token": USUARIOS_DB[usuario]["token"]}

    raise HTTPException(status_code=401, detail="Credenciales inválidas")

# Endpoint para registrar nuevos usuarios
class Registro(BaseModel):
    usuario: str
    password: str
    age: int

@app.post("/register")
def register(registro: Registro):
    if registro.usuario in USUARIOS_DB:
        raise HTTPException(status_code=400, detail="Usuario ya registrado")
    USUARIOS_DB[registro.usuario] = {"password": registro.password, "token": f"token{random.randint(100, 999)}"}
    return {"msg": "Usuario registrado exitosamente"}
