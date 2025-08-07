from modules.public.emparejamientos.application.services.emparejamiento_service import EmparejamientoService
from modules.public.emparejamientos.application.dto.emparejamiento_dto import EmparejamientoCreateDTO, EmparejamientoUpdateDTO

class EmparejamientoController:
    def __init__(self, service: EmparejamientoService):
        self.service = service

    def crear_emparejamiento(self, dto: EmparejamientoCreateDTO):
        return self.service.crear_emparejamiento(dto)

    def actualizar_emparejamiento(self, dto: EmparejamientoUpdateDTO):
        return self.service.actualizar_emparejamiento(dto)

    def listar_emparejamientos(self):
        return self.service.listar_emparejamientos()