from fastapi import FastAPI
from modules.private.robots.presentation.routes.robots_routes import router as robot_router
from modules.general.rol.presentation.routes.rol_routes import router as rol_router
from modules.general.usuarios.presentation.routes.usuario_routes import router as usuario_router


app = FastAPI()

app.include_router(robot_router, prefix="/api/robots")
app.include_router(rol_router, prefix="/api/roles")
app.include_router(usuario_router, prefix="/api/usuarios")
