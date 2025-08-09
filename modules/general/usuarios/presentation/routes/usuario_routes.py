from fastapi import APIRouter, Depends, HTTPException
from modules.general.usuarios.application.dto.usuario_dto import UsuarioOutDTO
from modules.general.usuarios.presentation.controllers.usuario_controller import UsuarioController
from modules.general.usuarios.application.dto.completar_usuario_dto import CompletarUsuarioDTO
from modules.general.usuarios.application.dto.usuario_create_web_dto import UsuarioCreateWebDTO
from modules.general.usuarios.application.dto.ingresar_usuario_dto import UsuarioCreateRobotDTO
from modules.general.usuarios.application.dto.usuario_dto import UsuarioOutDTO
from fastapi import Query

router = APIRouter()

def get_controller():
    return UsuarioController()

@router.post("/completar/", response_model=UsuarioOutDTO)
def completar_registro(dto: CompletarUsuarioDTO, controller: UsuarioController = Depends(get_controller)):
    usuario = controller.completar_registro(dto)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado o ya tiene contraseña")
    return usuario

@router.post("/web/", response_model=UsuarioOutDTO)
def crear_usuario_web(dto: UsuarioCreateWebDTO, controller: UsuarioController = Depends(get_controller)):
    usuario = controller.crear_usuario_web(dto)
    return usuario

@router.get("/", response_model=list[UsuarioOutDTO])
def obtener_usuarios(
    registro_key: str = Query(None, description="Buscar por registro_key"),
    controller: UsuarioController = Depends(get_controller)
):
    if registro_key:
        usuarios = controller.buscar_por_registro_key(registro_key)
        return usuarios
    return controller.listar_usuarios()


@router.post("/ingresar", response_model=UsuarioOutDTO)
def crear_usuario_robot(dto: UsuarioCreateRobotDTO, controller: UsuarioController = Depends(get_controller)):
    usuario = controller.crear_usuario_robot(dto)
    return UsuarioOutDTO.from_orm(usuario)