from fastapi import APIRouter, Depends
from modules.general.rol.application.dto.rol_dto import RolCreateDTO, RolOutDTO
from modules.general.rol.presentation.controllers.rol_controller import RolController

router = APIRouter()

def get_controller():
    return RolController()

@router.get("/", response_model=list[RolOutDTO])
def obtener_roles(controller: RolController = Depends(get_controller)):
    return controller.listar_roles()

@router.post("/", response_model=RolOutDTO)
def crear_rol(dto: RolCreateDTO, controller: RolController = Depends(get_controller)):
    return controller.crear_rol(dto)