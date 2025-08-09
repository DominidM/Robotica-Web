from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import modules.models  # Importar ANTES de las rutas

from modules.private.robots.presentation.routes.robots_routes import router as robot_router
from modules.general.rol.presentation.routes.rol_routes import router as rol_router
from modules.general.usuarios.presentation.routes.usuario_routes import router as usuario_router
from modules.public.sesiones.presentation.routes.sesiones_routes import router as sesiones_router
from modules.public.emparejamientos.presentation.routes.emparejamiento_routes import router as emparejamiento_router
from modules.public.emociones.presentation.routes.emociones_routes import router as emociones_router
from modules.public.mensajes.presentation.routes.mensajes_routes import router as mensajes_router

app = FastAPI()

# --- Habilitar CORS ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # O restringe a ["http://localhost:8000"] para mayor seguridad
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(robot_router, prefix="/api/robots")
app.include_router(rol_router, prefix="/api/roles")
app.include_router(usuario_router, prefix="/api/usuarios")
app.include_router(sesiones_router, prefix="/api/sesiones") 
app.include_router(emparejamiento_router, prefix="/api/emparejamientos")
app.include_router(emociones_router, prefix="/api/emociones")
app.include_router(mensajes_router, prefix="/api/mensajes")