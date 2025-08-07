from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from modules.public.mensajes.presentation.controllers.mensajes_controller import MensajesController
from modules.public.mensajes.application.dto.mensajes_dto import MensajeCreateDTO, MensajeOutDTO
from modules.public.mensajes.infrastructure.repositories.mensajes_repository import MensajesRepository
from modules.public.mensajes.application.services.mensajes_service import MensajesService
from modules.database import get_db

router = APIRouter()

def get_controller(db: Session = Depends(get_db)):
    repo = MensajesRepository(db)
    service = MensajesService(repo)
    return MensajesController(service)

@router.post("/", response_model=MensajeOutDTO)
def crear_mensaje(dto: MensajeCreateDTO, controller: MensajesController = Depends(get_controller)):
    return controller.crear_mensaje(dto)

@router.get("/", response_model=list[MensajeOutDTO])
def listar_mensajes(controller: MensajesController = Depends(get_controller)):
    return controller.listar_mensajes()