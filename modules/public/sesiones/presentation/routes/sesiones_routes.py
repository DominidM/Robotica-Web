from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from modules.public.sesiones.presentation.controllers.sesiones_controller import SesionesController
from modules.public.sesiones.application.dto.sesiones_dto import SesionCreateDTO, SesionOutDTO, SesionCloseDTO
from modules.public.sesiones.infrastructure.repositories.sesiones_repository import SesionesRepository
from modules.public.sesiones.application.services.sesiones_service import SesionesService
from modules.database import get_db

router = APIRouter()

def get_controller(db: Session = Depends(get_db)):
    repo = SesionesRepository(db)
    service = SesionesService(repo)
    return SesionesController(service)

@router.post("/", response_model=SesionOutDTO)
def crear_sesion(dto: SesionCreateDTO, controller: SesionesController = Depends(get_controller)):
    return controller.crear_sesion(dto)

@router.post("/cerrar/", response_model=SesionOutDTO)
def cerrar_sesion(dto: SesionCloseDTO, controller: SesionesController = Depends(get_controller)):
    sesion = controller.cerrar_sesion(dto)
    if not sesion:
        raise HTTPException(status_code=404, detail="Sesión no encontrada")
    return sesion

@router.get("/", response_model=list[SesionOutDTO])
def listar_sesiones(controller: SesionesController = Depends(get_controller)):
    return controller.listar_sesiones()