from modules.public.emparejamientos.domain.repositories.Iemparejamiento_repository import IEmparejamientoRepository
from modules.public.emparejamientos.application.dto.emparejamiento_dto import EmparejamientoCreateDTO, EmparejamientoUpdateDTO

class EmparejamientoService:
    def __init__(self, repository: IEmparejamientoRepository):
        self.repository = repository

    def crear_emparejamiento(self, dto: EmparejamientoCreateDTO):
        return self.repository.crear_emparejamiento(dto)

    def actualizar_emparejamiento(self, dto: EmparejamientoUpdateDTO):
        return self.repository.actualizar_emparejamiento(dto)

    def listar_emparejamientos(self):
        return self.repository.listar_emparejamientos()