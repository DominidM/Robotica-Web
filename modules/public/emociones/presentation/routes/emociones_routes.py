from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from modules.public.emociones.presentation.controllers.emociones_controller import EmocionesController
from modules.public.emociones.application.dto.emociones_dto import EmocionCreateDTO, EmocionOutDTO
from modules.public.emociones.infrastructure.repositories.emociones_repository import EmocionesRepository
from modules.public.emociones.application.services.emociones_service import EmocionesService
from modules.database import get_db

router = APIRouter()

def get_controller(db: Session = Depends(get_db)):
    repo = EmocionesRepository(db)
    service = EmocionesService(repo)
    return EmocionesController(service)

@router.post("/", response_model=EmocionOutDTO)
def crear_emocion(dto: EmocionCreateDTO, controller: EmocionesController = Depends(get_controller)):
    return controller.crear_emocion(dto)

@router.get("/", response_model=list[EmocionOutDTO])
def listar_emociones(controller: EmocionesController = Depends(get_controller)):
    return controller.listar_emociones()