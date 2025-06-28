"""
FastAPI - Aplicación de ejemplo para practicar Backend

Esta pequeña aplicación tiene dos endpoints:
1. POST /login: Recibe usuario y contraseña, y retorna un token si son válidos.
2. GET /datos: Requiere autenticación por token en el header. Retorna datos dummy si el token es válido.

Para correr este ejemplo:
1. Instala Poetry si no lo tienes: https://python-poetry.org/docs/#installation
2. Crea el entorno: `poetry init` y luego instala FastAPI y Uvicorn:
   poetry add fastapi uvicorn
3. Ejecuta el servidor con:
   poetry run uvicorn api_sample:app --reload

Luego puedes probar con curl o Postman los endpoints.
"""

from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Simulación de base de datos de usuarios y tokens
# NUNCA JAMÁs se deben guardar datos sensibles en el código. Esto es solo un ejemplo.
# Con datos sensibles me refiero a contraseñas, usuarios, tokens de accesos a servicios.
USUARIOS_DB = {
    "usuario1": {"password": "1234", "token": "token123"},
    "usuario2": {"password": "abcd", "token": "token456"},
}

# Datos dummy que queremos proteger con autenticación
DATOS_DUMMY = {
    "mensaje": "¡Bienvenido!",
    "notificaciones": 5,
    "rol": "estudiante",
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

    if (usuario in USUARIOS_DB) and (
        USUARIOS_DB.get(usuario).get("password") == password
    ):
        return {"token": USUARIOS_DB[usuario]["token"]}
    raise HTTPException(status_code=401, detail="Credenciales inválidas")


# Función para verificar el token
def verificar_token(token: str) -> bool:
    for datos in USUARIOS_DB.values():
        if datos["token"] == token:
            return True
    return False


# Endpoint protegido
@app.get("/datos")
def obtener_datos(Authorization: Optional[str] = Header(None)):
    if not Authorization:
        raise HTTPException(
            status_code=401, detail="Token requerido en el header Authorization"
        )

    token = Authorization.replace(
        "Bearer ", ""
    )  # Por convención se usa 'Bearer <token>'
    if not verificar_token(token):
        raise HTTPException(status_code=403, detail="Token inválido")

    return DATOS_DUMMY
