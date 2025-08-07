from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from modules.public.emparejamientos.presentation.controllers.emparejamiento_controller import EmparejamientoController
from modules.public.emparejamientos.application.dto.emparejamiento_dto import EmparejamientoCreateDTO, EmparejamientoOutDTO, EmparejamientoUpdateDTO
from modules.public.emparejamientos.infrastructure.repositories.emparejamiento_repository import EmparejamientoRepository
from modules.public.emparejamientos.application.services.emparejamiento_service import EmparejamientoService
from modules.database import get_db

router = APIRouter()

def get_controller(db: Session = Depends(get_db)):
    repo = EmparejamientoRepository(db)
    service = EmparejamientoService(repo)
    return EmparejamientoController(service)

@router.post("/", response_model=EmparejamientoOutDTO)
def crear_emparejamiento(dto: EmparejamientoCreateDTO, controller: EmparejamientoController = Depends(get_controller)):
    return controller.crear_emparejamiento(dto)

@router.put("/", response_model=EmparejamientoOutDTO)
def actualizar_emparejamiento(dto: EmparejamientoUpdateDTO, controller: EmparejamientoController = Depends(get_controller)):
    emp = controller.actualizar_emparejamiento(dto)
    if not emp:
        raise HTTPException(status_code=404, detail="Emparejamiento no encontrado")
    return emp

@router.get("/", response_model=list[EmparejamientoOutDTO])
def listar_emparejamientos(controller: EmparejamientoController = Depends(get_controller)):
    return controller.listar_emparejamientos()