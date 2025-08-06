from fastapi import APIRouter, Depends, HTTPException
from modules.general.usuarios.application.dto.usuario_dto import UsuarioOutDTO
from modules.general.usuarios.presentation.controllers.usuario_controller import UsuarioController
from modules.general.usuarios.application.dto.completar_usuario_dto import CompletarUsuarioDTO
from modules.general.usuarios.application.dto.usuario_create_web_dto import UsuarioCreateWebDTO
from modules.general.usuarios.application.dto.ingresar_usuario_dto import UsuarioCreateRobotDTO
from modules.general.usuarios.application.dto.usuario_dto import UsuarioOutDTO

router = APIRouter()

def get_controller():
    return UsuarioController()

@router.get("/", response_model=list[UsuarioOutDTO])
def obtener_usuarios(controller: UsuarioController = Depends(get_controller)):
    return controller.listar_usuarios()

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

@router.post("/ingresar", response_model=UsuarioOutDTO)
def crear_usuario_robot(dto: UsuarioCreateRobotDTO, controller: UsuarioController = Depends(get_controller)):
    usuario = controller.crear_usuario_robot(dto)
    return UsuarioOutDTO.from_orm(usuario)